from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Naytetietoja(Base):
    # Specimen information
    __tablename__ = 'naytetietoja'
    __table_args__ = (ForeignKeyConstraint(['hankintaID'], ['hankintatiedot.hankintaID'], name='naytetietoja_ibfk_1'), Index('IDX_Naytetietoja1', 'hankintaID'))
    # Specimen number
    naytteen_nro: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
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
    hankintaID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    # Location explanation
    sijainnin_selite: Mapped[Optional[str]] = mapped_column(String(255))
    # Reference number
    viitenro: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    # Reference explanation
    viitteen_selite: Mapped[Optional[str]] = mapped_column(String(255))
    # New specimen date
    uus_naytteen_paivays: Mapped[Optional[datetime.date]] = mapped_column(Date)
    # Acquisition data
    hankintatiedot: Mapped[Optional['Hankintatiedot']] = relationship('Hankintatiedot', back_populates='naytetietoja')
