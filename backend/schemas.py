from datetime import date, datetime
from typing import Literal, Optional
from pydantic import BaseModel, model_validator


PARTIES = ["smer", "ps", "hlas", "olano", "kdh", "sas", "sns", "rep", "ma", "dem", "sme_rodina"]
FIRMS = Literal["AKO", "Focus", "Ipsos", "NMS"]


class PollBase(BaseModel):
    firm: FIRMS
    date_str: str
    date: date
    smer: Optional[float] = None
    ps: Optional[float] = None
    hlas: Optional[float] = None
    olano: Optional[float] = None
    kdh: Optional[float] = None
    sas: Optional[float] = None
    sns: Optional[float] = None
    rep: Optional[float] = None
    ma: Optional[float] = None
    dem: Optional[float] = None
    sme_rodina: Optional[float] = None
    source: str = "manual"


class PollCreate(PollBase):
    @model_validator(mode="after")
    def validate_party_values(self) -> "PollCreate":
        valid = [
            v for party in PARTIES
            if (v := getattr(self, party)) is not None and 0 <= v <= 50
        ]
        if len(valid) < 3:
            raise ValueError("At least 3 party values must be non-null and between 0 and 50")
        return self


class PollUpdate(BaseModel):
    firm: Optional[FIRMS] = None
    date_str: Optional[str] = None
    date: Optional[date] = None
    smer: Optional[float] = None
    ps: Optional[float] = None
    hlas: Optional[float] = None
    olano: Optional[float] = None
    kdh: Optional[float] = None
    sas: Optional[float] = None
    sns: Optional[float] = None
    rep: Optional[float] = None
    ma: Optional[float] = None
    dem: Optional[float] = None
    sme_rodina: Optional[float] = None
    source: Optional[str] = None


class PollRead(PollBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
