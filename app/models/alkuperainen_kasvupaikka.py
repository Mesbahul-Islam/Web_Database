from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class AlkuperainenKasvupaikka(Base):
    # Original growing site
    __tablename__ = 'alkuperainen_kasvupaikka'
    __table_args__ = (ForeignKeyConstraint(['taksonin_nro'], ['taksoni.taksonin_nro'], name='alkuperainen_kasvupaikka_ibfk_1'), ForeignKeyConstraint(['viitenro'], ['viite.viitenro'], name='alkuperainen_kasvupaikka_ibfk_2'), Index('IDX_Alkuperainen_kasvupaikka1', 'taksonin_nro'), Index('IDX_Alkuperainen_kasvupaikka2', 'viitenro'))
    # Alkuperaisen growing site number
    alkuperaisen_kasvupaikan_nro: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Taxon number
    taksonin_nro: Mapped[int] = mapped_column(Integer, nullable=False, server_default=text('0'))
    # Original growing site
    alkuperainen_kasvupaikka: Mapped[Optional[str]] = mapped_column(String(255))
    # Growing site detail
    kasvupaikan_tarkenne: Mapped[Optional[str]] = mapped_column(String(255))
    # Reference number
    viitenro: Mapped[Optional[int]] = mapped_column(Integer)
    # Taxon
    taksoni: Mapped['Taksoni'] = relationship('Taksoni', back_populates='alkuperainen_kasvupaikka')
    # Reference or bibliographic citation
    viite: Mapped[Optional['Viite']] = relationship('Viite', back_populates='alkuperainen_kasvupaikka')
