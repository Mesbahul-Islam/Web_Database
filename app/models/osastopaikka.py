from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Osastopaikka(Base):
    # Section location
    __tablename__ = 'osastopaikka'
    __table_args__ = (ForeignKeyConstraint(['hankintaID'], ['hankintatiedot.hankintaID'], name='osastopaikka_ibfk_1'), Index('IDX_Osastopaikka1', 'hankintaID'))
    # Section number
    osaston_numero: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    # Section code
    osaston_koodi: Mapped[Optional[str]] = mapped_column(String(255))
    # Section name
    osaston_nimi: Mapped[Optional[str]] = mapped_column(String(255))
    # Plant status
    kasvin_status: Mapped[Optional[str]] = mapped_column(String(255))
    # Plant remarks
    kasvin_huomautuksia: Mapped[Optional[str]] = mapped_column(Text)
    # Acquisition ID
    hankintaID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    # Acquisition data
    hankintatiedot: Mapped[Optional['Hankintatiedot']] = relationship('Hankintatiedot', back_populates='osastopaikka')
    # Placement location
    sijoituspaikka: Mapped[list['Sijoituspaikka']] = relationship('Sijoituspaikka', back_populates='osastopaikka')
