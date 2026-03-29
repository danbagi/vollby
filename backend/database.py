from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite+aiosqlite:///./polls.db"

engine = create_async_engine(DATABASE_URL, echo=False)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session


async def init_db():
    from models import Poll  # noqa: F401
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await seed_db()


_SEED_DATA = [
    {"firm": "NMS",   "date_str": "4–9 Mar 2026",         "date": "2026-03-06", "ps": 21.4, "smer": 16.7, "hlas": 7.6,  "olano": 9.6, "kdh": 4.8,  "sas": 7.6,  "sns": 2.3,  "rep": 13.5, "ma": 4.2, "dem": 5.1, "sme_rodina": 3.6},
    {"firm": "Ipsos", "date_str": "16–20 Feb 2026",        "date": "2026-02-18", "ps": 18.8, "smer": 18.4, "hlas": 7.4,  "olano": 8.8, "kdh": None, "sas": 6.0,  "sns": None, "rep": 8.4, "ma": 2.8, "dem": 11.7, "sme_rodina": None},
    {"firm": "AKO",   "date_str": "10–19 Feb 2026",        "date": "2026-02-14", "ps": 20.6, "smer": 16.4, "hlas": 8.8,  "olano": 9.3, "kdh": None, "sas": 7.4,  "sns": None, "rep": 7.9, "ma": 4.8, "dem": 8.7,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "4–8 Feb 2026",          "date": "2026-02-06", "ps": 19.1, "smer": 17.6, "hlas": 6.2,  "olano": 7.5, "kdh": 2.3,  "sas": 4.9,  "sns": None, "rep": 7.4, "ma": 3.0, "dem": 13.4, "sme_rodina": None},
    {"firm": "Focus", "date_str": "3–9 Feb 2026",          "date": "2026-02-06", "ps": 19.3, "smer": 17.7, "hlas": 8.1,  "olano": 9.7, "kdh": None, "sas": 6.9,  "sns": None, "rep": 7.6, "ma": 4.1, "dem": 9.9,  "sme_rodina": None},
    {"firm": "Ipsos", "date_str": "15–20 Jan 2026",        "date": "2026-01-17", "ps": 20.5, "smer": 17.6, "hlas": 7.3,  "olano": 8.3, "kdh": None, "sas": 6.8,  "sns": None, "rep": 8.4, "ma": 2.4, "dem": 12.3, "sme_rodina": None},
    {"firm": "AKO",   "date_str": "13–20 Jan 2026",        "date": "2026-01-16", "ps": 23.2, "smer": 16.9, "hlas": 9.2,  "olano": 8.0, "kdh": None, "sas": 7.0,  "sns": None, "rep": 7.5, "ma": 4.7, "dem": 7.2,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "8–11 Jan 2026",         "date": "2026-01-09", "ps": 20.8, "smer": 17.8, "hlas": 6.5,  "olano": 7.2, "kdh": 2.0,  "sas": 6.4,  "sns": None, "rep": 6.0, "ma": 2.8, "dem": 12.9, "sme_rodina": None},
    {"firm": "AKO",   "date_str": "9–16 Dec 2025",         "date": "2025-12-12", "ps": 23.6, "smer": 17.0, "hlas": 9.6,  "olano": 8.9, "kdh": None, "sas": 6.6,  "sns": None, "rep": 7.4, "ma": 4.7, "dem": 7.0,  "sme_rodina": None},
    {"firm": "Focus", "date_str": "1–9 Dec 2025",          "date": "2025-12-05", "ps": 21.7, "smer": 17.4, "hlas": 8.8,  "olano": 8.4, "kdh": None, "sas": 7.2,  "sns": None, "rep": 6.7, "ma": 4.3, "dem": 9.3,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "28 Nov–2 Dec 2025",     "date": "2025-11-30", "ps": 22.6, "smer": 18.3, "hlas": 6.5,  "olano": 7.6, "kdh": 1.5,  "sas": 5.3,  "sns": None, "rep": 6.3, "ma": 2.2, "dem": 11.9, "sme_rodina": None},
    {"firm": "Ipsos", "date_str": "24–28 Nov 2025",        "date": "2025-11-26", "ps": 23.6, "smer": 17.8, "hlas": 7.8,  "olano": 9.5, "kdh": 1.0,  "sas": 5.5,  "sns": None, "rep": 6.7, "ma": 2.2, "dem": 10.7, "sme_rodina": None},
    {"firm": "Focus", "date_str": "11–18 Nov 2025",        "date": "2025-11-14", "ps": 22.1, "smer": 16.5, "hlas": 9.1,  "olano": 8.9, "kdh": None, "sas": 6.3,  "sns": None, "rep": 6.5, "ma": 4.2, "dem": 10.0, "sme_rodina": None},
    {"firm": "AKO",   "date_str": "11–18 Nov 2025",        "date": "2025-11-14", "ps": 23.3, "smer": 17.1, "hlas": 10.4, "olano": 8.2, "kdh": None, "sas": 6.5,  "sns": None, "rep": 7.5, "ma": 4.6, "dem": 6.9,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "5–9 Nov 2025",          "date": "2025-11-07", "ps": 23.1, "smer": 16.3, "hlas": 7.5,  "olano": 8.3, "kdh": 1.6,  "sas": 5.4,  "sns": None, "rep": 6.3, "ma": 2.4, "dem": 12.1, "sme_rodina": None},
    {"firm": "Ipsos", "date_str": "15–20 Oct 2025",        "date": "2025-10-17", "ps": 21.6, "smer": 18.5, "hlas": 9.1,  "olano": 7.8, "kdh": None, "sas": 6.5,  "sns": None, "rep": 7.3, "ma": 3.6, "dem": 10.0, "sme_rodina": None},
    {"firm": "Focus", "date_str": "13–21 Oct 2025",        "date": "2025-10-17", "ps": 23.1, "smer": 17.0, "hlas": 9.4,  "olano": 8.3, "kdh": None, "sas": 6.7,  "sns": None, "rep": 6.3, "ma": 4.3, "dem": 9.8,  "sme_rodina": None},
    {"firm": "AKO",   "date_str": "7–18 Oct 2025",         "date": "2025-10-12", "ps": 22.8, "smer": 17.9, "hlas": 10.8, "olano": 7.5, "kdh": None, "sas": 6.8,  "sns": None, "rep": 7.1, "ma": 4.5, "dem": 8.6,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "1–5 Oct 2025",          "date": "2025-10-03", "ps": 24.8, "smer": 17.9, "hlas": 8.3,  "olano": 6.4, "kdh": 1.4,  "sas": 5.4,  "sns": None, "rep": 5.9, "ma": 2.0, "dem": 11.8, "sme_rodina": None},
    {"firm": "Ipsos", "date_str": "17–21 Sep 2025",        "date": "2025-09-19", "ps": 22.8, "smer": 18.4, "hlas": 8.3,  "olano": 7.3, "kdh": None, "sas": 6.8,  "sns": None, "rep": 7.7, "ma": 3.5, "dem": 10.9, "sme_rodina": None},
    {"firm": "AKO",   "date_str": "8–22 Sep 2025",         "date": "2025-09-15", "ps": 23.1, "smer": 17.4, "hlas": 11.0, "olano": 8.7, "kdh": 0.2,  "sas": 7.2,  "sns": None, "rep": 7.4, "ma": 4.6, "dem": 8.2,  "sme_rodina": None},
    {"firm": "Focus", "date_str": "10–17 Sep 2025",        "date": "2025-09-13", "ps": 22.0, "smer": 18.2, "hlas": 9.7,  "olano": 8.5, "kdh": None, "sas": 6.1,  "sns": None, "rep": 6.1, "ma": 4.3, "dem": 9.7,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "3–7 Sep 2025",          "date": "2025-09-05", "ps": 22.1, "smer": 20.1, "hlas": 9.5,  "olano": 7.1, "kdh": 1.7,  "sas": 5.7,  "sns": None, "rep": 6.1, "ma": 2.0, "dem": 10.2, "sme_rodina": None},
    {"firm": "Ipsos", "date_str": "15–19 Aug 2025",        "date": "2025-08-17", "ps": 22.5, "smer": 20.0, "hlas": 9.8,  "olano": 7.5, "kdh": 0.9,  "sas": 6.0,  "sns": None, "rep": 7.1, "ma": 2.7, "dem": 10.3, "sme_rodina": None},
    {"firm": "Focus", "date_str": "6–19 Aug 2025",         "date": "2025-08-12", "ps": 21.2, "smer": 18.7, "hlas": 10.1, "olano": 8.2, "kdh": None, "sas": 6.7,  "sns": None, "rep": 6.3, "ma": 4.4, "dem": 9.9,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "6–10 Aug 2025",         "date": "2025-08-08", "ps": 23.9, "smer": 17.4, "hlas": 9.2,  "olano": 8.2, "kdh": 1.8,  "sas": 6.0,  "sns": None, "rep": 6.2, "ma": 2.7, "dem": 10.4, "sme_rodina": None},
    {"firm": "AKO",   "date_str": "5–11 Aug 2025",         "date": "2025-08-08", "ps": 22.1, "smer": 18.2, "hlas": 11.3, "olano": 7.6, "kdh": None, "sas": 7.1,  "sns": None, "rep": 7.9, "ma": 4.5, "dem": 7.4,  "sme_rodina": None},
    {"firm": "AKO",   "date_str": "8–15 Jul 2025",         "date": "2025-07-11", "ps": 22.1, "smer": 19.4, "hlas": 12.4, "olano": 8.3, "kdh": None, "sas": 6.6,  "sns": None, "rep": 7.5, "ma": 4.2, "dem": 8.0,  "sme_rodina": None},
    {"firm": "Focus", "date_str": "7–13 Jul 2025",         "date": "2025-07-10", "ps": 20.7, "smer": 19.6, "hlas": 11.7, "olano": 7.5, "kdh": None, "sas": 6.3,  "sns": None, "rep": 6.8, "ma": 3.8, "dem": 9.8,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "2–7 Jul 2025",          "date": "2025-07-04", "ps": 20.9, "smer": 18.1, "hlas": 9.7,  "olano": 7.1, "kdh": 2.8,  "sas": 6.2,  "sns": None, "rep": 6.7, "ma": 2.9, "dem": 10.3, "sme_rodina": None},
    {"firm": "Ipsos", "date_str": "16–19 Jun 2025",        "date": "2025-06-17", "ps": 21.7, "smer": 19.7, "hlas": 10.3, "olano": 7.3, "kdh": None, "sas": 6.3,  "sns": None, "rep": 6.1, "ma": 2.5, "dem": 9.9,  "sme_rodina": None},
    {"firm": "AKO",   "date_str": "11–19 Jun 2025",        "date": "2025-06-15", "ps": 22.5, "smer": 19.3, "hlas": 12.1, "olano": 8.0, "kdh": None, "sas": 6.9,  "sns": None, "rep": 7.3, "ma": 4.1, "dem": 8.1,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "4–8 Jun 2025",          "date": "2025-06-06", "ps": 23.0, "smer": 19.8, "hlas": 9.0,  "olano": 7.1, "kdh": 3.0,  "sas": 6.4,  "sns": None, "rep": 5.7, "ma": 2.5, "dem": 9.4,  "sme_rodina": None},
    {"firm": "Focus", "date_str": "2–9 Jun 2025",          "date": "2025-06-05", "ps": 20.2, "smer": 18.8, "hlas": 10.5, "olano": 8.5, "kdh": None, "sas": 7.5,  "sns": None, "rep": 6.1, "ma": 3.7, "dem": 9.7,  "sme_rodina": None},
    {"firm": "AKO",   "date_str": "19–26 May 2025",        "date": "2025-05-22", "ps": 21.5, "smer": 19.0, "hlas": 12.1, "olano": 8.8, "kdh": None, "sas": 7.8,  "sns": None, "rep": 7.2, "ma": 4.2, "dem": 7.3,  "sme_rodina": None},
    {"firm": "Focus", "date_str": "12–19 May 2025",        "date": "2025-05-15", "ps": 20.9, "smer": 19.1, "hlas": 10.6, "olano": 7.8, "kdh": None, "sas": 7.3,  "sns": None, "rep": 6.8, "ma": 3.9, "dem": 7.9,  "sme_rodina": None},
    {"firm": "Ipsos", "date_str": "12–16 May 2025",        "date": "2025-05-14", "ps": 21.9, "smer": 19.6, "hlas": 8.4,  "olano": 7.3, "kdh": 1.3,  "sas": 7.5,  "sns": None, "rep": 6.6, "ma": 3.0, "dem": 9.3,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "30 Apr–4 May 2025",     "date": "2025-05-02", "ps": 22.8, "smer": 20.6, "hlas": 8.9,  "olano": 7.7, "kdh": 1.5,  "sas": 6.4,  "sns": None, "rep": 6.1, "ma": 2.3, "dem": 8.8,  "sme_rodina": None},
    {"firm": "AKO",   "date_str": "10–17 Apr 2025",        "date": "2025-04-13", "ps": 22.5, "smer": 20.5, "hlas": 12.0, "olano": 8.7, "kdh": 0.1,  "sas": 7.3,  "sns": None, "rep": 7.1, "ma": 4.1, "dem": 7.0,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "2–6 Apr 2025",          "date": "2025-04-04", "ps": 23.4, "smer": 19.9, "hlas": 8.5,  "olano": 6.8, "kdh": 2.3,  "sas": 6.9,  "sns": None, "rep": 6.5, "ma": 1.9, "dem": 9.2,  "sme_rodina": None},
    {"firm": "Focus", "date_str": "1–8 Apr 2025",          "date": "2025-04-04", "ps": 21.0, "smer": 19.3, "hlas": 10.9, "olano": 7.3, "kdh": None, "sas": 8.4,  "sns": None, "rep": 6.6, "ma": 3.9, "dem": 8.2,  "sme_rodina": None},
    {"firm": "AKO",   "date_str": "11–19 Mar 2025",        "date": "2025-03-15", "ps": 21.7, "smer": 21.2, "hlas": 12.3, "olano": 7.3, "kdh": None, "sas": 7.8,  "sns": None, "rep": 6.6, "ma": 4.0, "dem": 7.3,  "sme_rodina": None},
    {"firm": "Ipsos", "date_str": "10–14 Mar 2025",        "date": "2025-03-12", "ps": 21.4, "smer": 22.1, "hlas": 12.5, "olano": 5.9, "kdh": None, "sas": 7.8,  "sns": None, "rep": 6.3, "ma": 2.0, "dem": 7.4,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "5–9 Mar 2025",          "date": "2025-03-07", "ps": 23.8, "smer": 21.4, "hlas": 8.8,  "olano": 6.8, "kdh": 2.2,  "sas": 6.0,  "sns": None, "rep": 6.2, "ma": 2.0, "dem": 8.1,  "sme_rodina": None},
    {"firm": "Focus", "date_str": "7–12 Feb 2025",         "date": "2025-02-09", "ps": 22.1, "smer": 21.7, "hlas": 11.8, "olano": 5.6, "kdh": 0.6,  "sas": 7.8,  "sns": None, "rep": 6.2, "ma": 3.7, "dem": 7.8,  "sme_rodina": None},
    {"firm": "AKO",   "date_str": "5–12 Feb 2025",         "date": "2025-02-08", "ps": 24.1, "smer": 22.1, "hlas": 12.5, "olano": 6.0, "kdh": None, "sas": 6.9,  "sns": None, "rep": 6.4, "ma": 4.1, "dem": 5.7,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "5–9 Feb 2025",          "date": "2025-02-07", "ps": 24.6, "smer": 22.5, "hlas": 10.5, "olano": 5.8, "kdh": 2.1,  "sas": 6.6,  "sns": None, "rep": 6.1, "ma": 1.5, "dem": 7.4,  "sme_rodina": None},
    {"firm": "AKO",   "date_str": "14–24 Jan 2025",        "date": "2025-01-19", "ps": 24.6, "smer": 22.5, "hlas": 13.0, "olano": 5.4, "kdh": 0.3,  "sas": 6.7,  "sns": None, "rep": 7.1, "ma": 4.2, "dem": 5.1,  "sme_rodina": None},
    {"firm": "Ipsos", "date_str": "11–17 Jan 2025",        "date": "2025-01-14", "ps": 23.0, "smer": 22.2, "hlas": 11.1, "olano": 5.6, "kdh": 1.9,  "sas": 7.3,  "sns": None, "rep": 6.3, "ma": 2.0, "dem": 7.7,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "9–13 Jan 2025",         "date": "2025-01-11", "ps": 23.9, "smer": 18.4, "hlas": 11.5, "olano": 6.3, "kdh": 2.3,  "sas": 5.9,  "sns": None, "rep": 6.7, "ma": 2.1, "dem": 8.9,  "sme_rodina": None},
    {"firm": "AKO",   "date_str": "16–19 Dec 2024",        "date": "2024-12-17", "ps": 22.8, "smer": 20.3, "hlas": 13.9, "olano": 6.2, "kdh": 0.2,  "sas": 7.3,  "sns": None, "rep": 6.6, "ma": 4.6, "dem": 5.4,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "4–9 Dec 2024",          "date": "2024-12-06", "ps": 24.8, "smer": 19.1, "hlas": 10.7, "olano": 6.5, "kdh": 2.9,  "sas": 5.5,  "sns": None, "rep": 4.8, "ma": 2.9, "dem": 9.5,  "sme_rodina": None},
    {"firm": "Focus", "date_str": "2–8 Dec 2024",          "date": "2024-12-05", "ps": 21.5, "smer": 20.8, "hlas": 13.8, "olano": 5.2, "kdh": None, "sas": 6.9,  "sns": None, "rep": 6.1, "ma": 3.7, "dem": 8.1,  "sme_rodina": None},
    {"firm": "AKO",   "date_str": "12–20 Nov 2024",        "date": "2024-11-16", "ps": 21.2, "smer": 20.7, "hlas": 14.7, "olano": 6.6, "kdh": None, "sas": 6.7,  "sns": None, "rep": 6.9, "ma": 4.7, "dem": 5.9,  "sme_rodina": None},
    {"firm": "Focus", "date_str": "6–13 Nov 2024",         "date": "2024-11-09", "ps": 22.6, "smer": 21.9, "hlas": 13.3, "olano": 3.6, "kdh": None, "sas": 6.2,  "sns": None, "rep": 6.7, "ma": 3.6, "dem": 8.6,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "7–11 Nov 2024",         "date": "2024-11-09", "ps": 25.1, "smer": 19.1, "hlas": 10.8, "olano": 4.7, "kdh": 1.0,  "sas": 6.4,  "sns": None, "rep": 6.0, "ma": 3.3, "dem": 8.7,  "sme_rodina": None},
    {"firm": "Ipsos", "date_str": "27 Oct–1 Nov 2024",     "date": "2024-10-29", "ps": 22.6, "smer": 21.9, "hlas": 12.8, "olano": 3.6, "kdh": 1.6,  "sas": 6.9,  "sns": None, "rep": 6.2, "ma": 2.4, "dem": 7.7,  "sme_rodina": None},
    {"firm": "AKO",   "date_str": "8–17 Oct 2024",         "date": "2024-10-12", "ps": 21.3, "smer": 21.3, "hlas": 15.0, "olano": 5.9, "kdh": None, "sas": 6.2,  "sns": None, "rep": 6.5, "ma": 3.4, "dem": 4.7,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "2–7 Oct 2024",          "date": "2024-10-04", "ps": 24.4, "smer": 20.5, "hlas": 12.0, "olano": 5.2, "kdh": 0.2,  "sas": 6.9,  "sns": None, "rep": 6.2, "ma": 2.9, "dem": 7.4,  "sme_rodina": None},
    {"firm": "Focus", "date_str": "17–26 Sep 2024",        "date": "2024-09-21", "ps": 22.1, "smer": 23.3, "hlas": 12.8, "olano": 4.1, "kdh": None, "sas": 6.0,  "sns": None, "rep": 5.6, "ma": 4.7, "dem": 7.9,  "sme_rodina": None},
    {"firm": "AKO",   "date_str": "10–16 Sep 2024",        "date": "2024-09-13", "ps": 22.4, "smer": 22.8, "hlas": 15.1, "olano": 3.9, "kdh": None, "sas": 6.8,  "sns": None, "rep": 6.4, "ma": 4.9, "dem": 5.4,  "sme_rodina": None},
    {"firm": "Ipsos", "date_str": "6–10 Sep 2024",         "date": "2024-09-08", "ps": 21.6, "smer": 25.5, "hlas": 11.9, "olano": 4.9, "kdh": None, "sas": 6.0,  "sns": None, "rep": 7.0, "ma": 3.4, "dem": 6.3,  "sme_rodina": None},
    {"firm": "NMS",   "date_str": "5–9 Sep 2024",          "date": "2024-09-07", "ps": 24.5, "smer": 23.9, "hlas": 12.6, "olano": 4.5, "kdh": 6.2,  "sas": 6.1,  "sns": 3.5, "rep": 6.1, "ma": 3.4, "dem": 3.3,  "sme_rodina": 3.9,}
]


async def seed_db():
    from datetime import date as date_type
    from models import Poll
    from sqlalchemy import select, func

    async with SessionLocal() as session:
        count = await session.scalar(select(func.count()).select_from(Poll))
        if count and count > 0:
            return

        for row in _SEED_DATA:
            poll = Poll(
                firm=row["firm"],
                date_str=row["date_str"],
                date=date_type.fromisoformat(row["date"]),
                ps=row["ps"],
                smer=row["smer"],
                hlas=row["hlas"],
                olano=row["olano"],
                kdh=row["kdh"],
                sas=row["sas"],
                sns=row["sns"],
                rep=row["rep"],
                ma=row["ma"],
                dem=row["dem"],
                sme_rodina=row["sme_rodina"],
                source="manual",
            )
            session.add(poll)
        await session.commit()
