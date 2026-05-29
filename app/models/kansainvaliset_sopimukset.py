from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class KansainvalisetSopimukset(Base):
    # International agreements
    __tablename__ = 'kansainvaliset_sopimukset'
    __table_args__ = (ForeignKeyConstraint(['taksonin_nro'], ['taksoni.taksonin_nro'], name='kansainvaliset_sopimukset_ibfk_1'), ForeignKeyConstraint(['viitenro'], ['viite.viitenro'], name='kansainvaliset_sopimukset_ibfk_2'), Index('IDX_Kansainvaliset_Sopimukset1', 'taksonin_nro'), Index('IDX_Kansainvaliset_Sopimukset2', 'viitenro'))
    # Agreement ID
    sopimus_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Taxon number
    taksonin_nro: Mapped[int] = mapped_column(Integer, nullable=False, server_default=text('0'))
    # Agreement name
    Sopimuksen_nimi: Mapped[Optional[str]] = mapped_column(String(255))
    # Explanation
    selite: Mapped[Optional[str]] = mapped_column(String(255))
    # Reference number
    viitenro: Mapped[Optional[int]] = mapped_column(Integer)
    # Taxon
    taksoni: Mapped['Taksoni'] = relationship('Taksoni', back_populates='kansainvaliset_sopimukset')
    # Reference or bibliographic citation
    viite: Mapped[Optional['Viite']] = relationship('Viite', back_populates='kansainvaliset_sopimukset')
