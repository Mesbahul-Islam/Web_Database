from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Tarkastusmerkinta(Base):
    # Inspection record
    __tablename__ = 'tarkastusmerkinta'
    __table_args__ = (ForeignKeyConstraint(['sijoituspaikan_nro'], ['sijoituspaikka.sijoituspaikan_nro'], name='tarkastusmerkinta_ibfk_1'), Index('IDX_Tarkastusmerkinta1', 'sijoituspaikan_nro'))
    # Tarkastusnro
    tarkastusnro: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Inspection date
    tarkastuspvm: Mapped[Optional[str]] = mapped_column(String(255))
    # Living individuals
    elavia_yksiloita: Mapped[Optional[str]] = mapped_column(String(255))
    # Observations about performance
    menestymista_koskevat_havainnot: Mapped[Optional[str]] = mapped_column(String(255))
    # Inspector
    tarkastaja: Mapped[Optional[str]] = mapped_column(String(255))
    # Plant remarks
    kasvin_huomautuksia: Mapped[Optional[str]] = mapped_column(Text)
    # Placement location number
    sijoituspaikan_nro: Mapped[Optional[int]] = mapped_column(Integer)
    # New inspection date
    uus_tarkastuspvm: Mapped[Optional[datetime.date]] = mapped_column(Date)
    # Placement location
    sijoituspaikka: Mapped[Optional['Sijoituspaikka']] = relationship('Sijoituspaikka', back_populates='tarkastusmerkinta')
