from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class SuomalainenLevinneisyysalue(Base):
    # Distribution area in Finland
    __tablename__ = 'suomalainen_levinneisyysalue'
    __table_args__ = (ForeignKeyConstraint(['taksonin_nro'], ['taksoni.taksonin_nro'], name='suomalainen_levinneisyysalue_ibfk_1'), ForeignKeyConstraint(['viitenro'], ['viite.viitenro'], name='suomalainen_levinneisyysalue_ibfk_2'), Index('IDX_Suomalainen_Levinneisyysalue1', 'taksonin_nro'), Index('IDX_Suomalainen_Levinneisyysalue2', 'viitenro'))
    # Distribution area number
    levinneisyysalueen_nro: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Taxon number
    taksonin_nro: Mapped[int] = mapped_column(Integer, nullable=False, server_default=text('0'))
    # Distribution area
    levinneisyysalue: Mapped[Optional[str]] = mapped_column(String(255))
    # Distribution area detail
    levinneisyysalueen_tarkenne: Mapped[Optional[str]] = mapped_column(String(255))
    # Native or introduced
    alkuperainen_vai_tulokas: Mapped[Optional[str]] = mapped_column(String(255))
    # Reference number
    viitenro: Mapped[Optional[int]] = mapped_column(Integer)
    # Taxon
    taksoni: Mapped['Taksoni'] = relationship('Taksoni', back_populates='suomalainen_levinneisyysalue')
    # Reference or bibliographic citation
    viite: Mapped[Optional['Viite']] = relationship('Viite', back_populates='suomalainen_levinneisyysalue')
