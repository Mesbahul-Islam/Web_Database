from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class KasvinKayttotarkoitus(Base):
    # Plant usage purpose
    __tablename__ = 'kasvin_kayttotarkoitus'
    __table_args__ = (ForeignKeyConstraint(['taksonin_nro'], ['taksoni.taksonin_nro'], name='kasvin_kayttotarkoitus_ibfk_1'), ForeignKeyConstraint(['viitenro'], ['viite.viitenro'], name='kasvin_kayttotarkoitus_ibfk_2'), Index('IDX_Kasvin_kayttotarkoitus1', 'taksonin_nro'), Index('IDX_Kasvin_kayttotarkoitus2', 'viitenro'))
    # Usage number
    kayttonro: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    # Taxon number
    taksonin_nro: Mapped[int] = mapped_column(INTEGER(11), nullable=False, server_default=text('0'))
    # Usage code
    kayton_tunnus: Mapped[Optional[str]] = mapped_column(String(255))
    # Usage
    kaytto: Mapped[Optional[str]] = mapped_column(String(255))
    # Explanation
    selite: Mapped[Optional[str]] = mapped_column(String(255))
    # Reference number
    viitenro: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    # Taxon
    taksoni: Mapped['Taksoni'] = relationship('Taksoni', back_populates='kasvin_kayttotarkoitus')
    # Reference or bibliographic citation
    viite: Mapped[Optional['Viite']] = relationship('Viite', back_populates='kasvin_kayttotarkoitus')
