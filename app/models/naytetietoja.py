from .base import Base, TimestampMixin, SafeDate
from typing import Optional
import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy import Column, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Naytetietoja(Base, TimestampMixin):
    # Specimen information
    __tablename__ = 'naytetietoja'
    __table_args__ = (ForeignKeyConstraint(['hankintaID'], ['hankintatiedot.hankintaID'], name='naytetietoja_ibfk_1'), Index('IDX_Naytetietoja1', 'hankintaID'))
    # Specimen number
    naytteen_nro: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Specimen type
    naytteen_tyyppi: Mapped[Optional[str]] = mapped_column(String(255))
    # Specimen location
    naytteen_sijainti: Mapped[Optional[str]] = mapped_column(String(255))
    # Specimen information
    naytteen_tiedot: Mapped[Optional[str]] = mapped_column(Text)
    # Specimen collector
    naytteen_keraaja: Mapped[Optional[str]] = mapped_column(String(255))
    # Specimen date
    naytteen_paivays: Mapped[Optional[str]] = mapped_column(String(255))
    # Acquisition ID
    hankintaID: Mapped[Optional[int]] = mapped_column(Integer)
    # Location explanation
    sijainnin_selite: Mapped[Optional[str]] = mapped_column(String(255))
    # Reference number
    viitenro: Mapped[Optional[int]] = mapped_column(Integer)
    # Reference explanation
    viitteen_selite: Mapped[Optional[str]] = mapped_column(String(255))
    # New specimen date
    uus_naytteen_paivays: Mapped[Optional[datetime.date]] = mapped_column(SafeDate)
    # Acquisition data
    hankintatiedot: Mapped[Optional['Hankintatiedot']] = relationship('Hankintatiedot', back_populates='naytetietoja')

