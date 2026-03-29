from datetime import date, datetime
from sqlalchemy import Date, DateTime, Float, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Poll(Base):
    __tablename__ = "polls"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    firm: Mapped[str] = mapped_column(String, nullable=False)
    date_str: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[date] = mapped_column(Date, nullable=False)

    smer: Mapped[float | None] = mapped_column(Float, nullable=True)
    ps: Mapped[float | None] = mapped_column(Float, nullable=True)
    hlas: Mapped[float | None] = mapped_column(Float, nullable=True)
    olano: Mapped[float | None] = mapped_column(Float, nullable=True)
    kdh: Mapped[float | None] = mapped_column(Float, nullable=True)
    sas: Mapped[float | None] = mapped_column(Float, nullable=True)
    sns: Mapped[float | None] = mapped_column(Float, nullable=True)
    rep: Mapped[float | None] = mapped_column(Float, nullable=True)
    ma: Mapped[float | None] = mapped_column(Float, nullable=True)
    dem: Mapped[float | None] = mapped_column(Float, nullable=True)
    sme_rodina: Mapped[float | None] = mapped_column(Float, nullable=True)

    source: Mapped[str] = mapped_column(String, default="manual", nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
