from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Synonyymi(Base):
    # Synonym
    __tablename__ = 'synonyymi'
    __table_args__ = (ForeignKeyConstraint(['taksonin_nro'], ['taksoni.taksonin_nro'], name='synonyymi_ibfk_1'), ForeignKeyConstraint(['viitenro'], ['viite.viitenro'], name='synonyymi_ibfk_2'), Index('IDX_Synonyymi1', 'taksonin_nro'), Index('IDX_Synonyymi2', 'viitenro'))
    # Synonyymin number
    synonyymin_nro: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    # Taxon number
    taksonin_nro: Mapped[int] = mapped_column(INTEGER(11), nullable=False, server_default=text('0'))
    # Name
    nimi: Mapped[Optional[str]] = mapped_column(String(255))
    # Author
    auktori: Mapped[Optional[str]] = mapped_column(String(255))
    # Reference number
    viitenro: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    # Reference or bibliographic citation 2
    viite_2: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    # Taxon
    taksoni: Mapped['Taksoni'] = relationship('Taksoni', back_populates='synonyymi')
    # Reference or bibliographic citation
    viite: Mapped[Optional['Viite']] = relationship('Viite', back_populates='synonyymi')
