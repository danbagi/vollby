from contextlib import asynccontextmanager
from datetime import date
from typing import Any, Dict, List, Optional

import httpx
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import delete, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db, init_db
from models import Poll
from schemas import FIRMS, PollCreate, PollRead, PollUpdate
from wiki_parser import parse_polls_from_wikitext

WIKI_API_URL = (
    "https://en.wikipedia.org/w/api.php"
    "?action=query"
    "&titles=Opinion_polling_for_the_next_Slovak_parliamentary_election"
    "&prop=revisions"
    "&rvprop=content"
    "&format=json"
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(title="voll.by", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", response_model=Dict[str, Any])
async def health(db: AsyncSession = Depends(get_db)):
    poll_count = await db.scalar(select(func.count()).select_from(Poll))
    latest_date = await db.scalar(select(func.max(Poll.date)))
    return {
        "status": "ok",
        "poll_count": poll_count or 0,
        "latest_date": str(latest_date) if latest_date else None,
    }


@app.get("/polls/latest", response_model=List[PollRead])
async def latest_polls(db: AsyncSession = Depends(get_db)):
    """Most recent poll per agency (up to 4 rows)."""
    subq = (
        select(Poll.firm, func.max(Poll.date).label("max_date"))
        .group_by(Poll.firm)
        .subquery()
    )
    stmt = (
        select(Poll)
        .join(subq, (Poll.firm == subq.c.firm) & (Poll.date == subq.c.max_date))
        .order_by(Poll.date.desc())
    )
    result = await db.execute(stmt)
    return result.scalars().all()


@app.get("/polls", response_model=List[PollRead])
async def list_polls(
    firm: Optional[str] = None,
    limit: int = 200,
    db: AsyncSession = Depends(get_db),
):
    stmt = select(Poll).order_by(Poll.date.desc(), Poll.id.desc()).limit(limit)
    if firm:
        stmt = stmt.where(Poll.firm == firm)
    result = await db.execute(stmt)
    return result.scalars().all()


@app.post("/polls/fetch-wiki")
async def fetch_wiki(db: AsyncSession = Depends(get_db)):
    """Fetch the Wikipedia polling page and insert any new rows."""
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            resp = await client.get(WIKI_API_URL)
            resp.raise_for_status()
        except httpx.HTTPError as exc:
            raise HTTPException(status_code=502, detail=f"Wikipedia request failed: {exc}")

    data = resp.json()
    pages = data.get("query", {}).get("pages", {})
    if not pages:
        raise HTTPException(status_code=502, detail="Empty pages in Wikipedia response")

    page = next(iter(pages.values()))
    revisions = page.get("revisions", [])
    if not revisions:
        raise HTTPException(status_code=502, detail="No revisions in Wikipedia response")

    rev = revisions[0]
    wikitext: str = rev.get("*") or (
        (rev.get("slots") or {}).get("main") or {}
    ).get("*", "")
    if not wikitext:
        raise HTTPException(status_code=502, detail="Could not extract wikitext")

    parsed = parse_polls_from_wikitext(wikitext)

    cutoff = date(2023, 10, 1)
    added = 0
    new_polls: list[dict] = []

    for p in parsed:
        # Date cutoff
        if p["date"] < cutoff:
            continue
        # Sanity checks on ps and smer
        ps = p.get("ps")
        smer = p.get("smer")
        if ps is None or not (3 <= ps <= 40):
            continue
        if smer is None or not (3 <= smer <= 40):
            continue
        # Deduplication: skip if firm+date_str already in db
        exists = await db.scalar(
            select(func.count())
            .select_from(Poll)
            .where(Poll.firm == p["firm"], Poll.date_str == p["date_str"])
        )
        if exists:
            continue

        poll = Poll(**p)
        db.add(poll)
        await db.flush()
        await db.refresh(poll)
        new_polls.append(PollRead.model_validate(poll).model_dump(mode="json"))
        added += 1

    await db.commit()

    total = await db.scalar(select(func.count()).select_from(Poll))
    return {"added": added, "total": total, "new_polls": new_polls}


@app.get("/polls/{poll_id}", response_model=PollRead)
async def get_poll(poll_id: int, db: AsyncSession = Depends(get_db)):
    poll = await db.get(Poll, poll_id)
    if not poll:
        raise HTTPException(status_code=404, detail="Poll not found")
    return poll


@app.post("/polls", response_model=PollRead, status_code=201)
async def create_poll(payload: PollCreate, db: AsyncSession = Depends(get_db)):
    poll = Poll(**payload.model_dump())
    db.add(poll)
    await db.commit()
    await db.refresh(poll)
    return poll


@app.patch("/polls/{poll_id}", response_model=PollRead)
async def update_poll(
    poll_id: int, payload: PollUpdate, db: AsyncSession = Depends(get_db)
):
    poll = await db.get(Poll, poll_id)
    if not poll:
        raise HTTPException(status_code=404, detail="Poll not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(poll, field, value)
    await db.commit()
    await db.refresh(poll)
    return poll


@app.delete("/polls/{poll_id}", status_code=204)
async def delete_poll(poll_id: int, db: AsyncSession = Depends(get_db)):
    poll = await db.get(Poll, poll_id)
    if not poll:
        raise HTTPException(status_code=404, detail="Poll not found")
    await db.delete(poll)
    await db.commit()


@app.delete("/polls", status_code=204)
async def delete_all_polls(
    source: Optional[str] = None, db: AsyncSession = Depends(get_db)
):
    stmt = delete(Poll)
    if source:
        stmt = stmt.where(Poll.source == source)
    await db.execute(stmt)
    await db.commit()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
