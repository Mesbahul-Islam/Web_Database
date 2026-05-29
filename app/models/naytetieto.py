from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Naytetieto(Base):
    # Specimen data
    __tablename__ = 'naytetieto'
    __table_args__ = (ForeignKeyConstraint(['taksonin_nro'], ['taksoni.taksonin_nro'], name='naytetieto_ibfk_1'), ForeignKeyConstraint(['viitenro'], ['viite.viitenro'], name='naytetieto_ibfk_2'), Index('IDX_Naytetieto1', 'taksonin_nro'), Index('IDX_Naytetieto2', 'viitenro'))
    # Specimen number
    naytteen_nro: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Taxon number
    taksonin_nro: Mapped[int] = mapped_column(Integer, nullable=False, server_default=text('0'))
    # Type
    tyyppi: Mapped[Optional[str]] = mapped_column(String(255))
    # Location
    sijainti: Mapped[Optional[str]] = mapped_column(String(255))
    # Information
    tiedot: Mapped[Optional[str]] = mapped_column(Text)
    # Collector
    keraaja: Mapped[Optional[str]] = mapped_column(String(255))
    # Date
    paivays: Mapped[Optional[str]] = mapped_column(String(255))
    # Reference number
    viitenro: Mapped[Optional[int]] = mapped_column(Integer)
    # Location explanation
    sijainnin_selite: Mapped[Optional[str]] = mapped_column(String(255))
    # Reference explanation
    viitteen_selite: Mapped[Optional[str]] = mapped_column(String(255))
    # Taxon
    taksoni: Mapped['Taksoni'] = relationship('Taksoni', back_populates='naytetieto')
    # Reference or bibliographic citation
    viite: Mapped[Optional['Viite']] = relationship('Viite', back_populates='naytetieto')
