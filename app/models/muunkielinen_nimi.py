from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class MuunkielinenNimi(Base):
    # Foreign-language name
    __tablename__ = 'muunkielinen_nimi'
    __table_args__ = (ForeignKeyConstraint(['taksonin_nro'], ['taksoni.taksonin_nro'], name='muunkielinen_nimi_ibfk_1'), ForeignKeyConstraint(['viitenro'], ['viite.viitenro'], name='muunkielinen_nimi_ibfk_2'), Index('IDX_Muunkielinen_nimi1', 'taksonin_nro'), Index('IDX_Muunkielinen_nimi2', 'viitenro'))
    # Nimen number
    nimen_nro: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    # Taxon number
    taksonin_nro: Mapped[int] = mapped_column(INTEGER(11), nullable=False, server_default=text('0'))
    # Name
    nimi: Mapped[Optional[str]] = mapped_column(String(255))
    # Kieli
    kieli: Mapped[Optional[str]] = mapped_column(String(255))
    # Reference number
    viitenro: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    # Reference or bibliographic citation 2
    viite_2: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    # Taxon
    taksoni: Mapped['Taksoni'] = relationship('Taksoni', back_populates='muunkielinen_nimi')
    # Reference or bibliographic citation
    viite: Mapped[Optional['Viite']] = relationship('Viite', back_populates='muunkielinen_nimi')
