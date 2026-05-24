from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class MaailmanLevinneisyysalue(Base):
    # World distribution area
    __tablename__ = 'maailman_levinneisyysalue'
    __table_args__ = (ForeignKeyConstraint(['taksonin_nro'], ['taksoni.taksonin_nro'], name='maailman_levinneisyysalue_ibfk_1'), Index('IDX_Maailman_Levinneisyysalue1', 'taksonin_nro'))
    # World distribution area number
    levinneisyysalueen_nro: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    # Taxon number
    taksonin_nro: Mapped[int] = mapped_column(INTEGER(11), nullable=False, server_default=text('0'))
    # Distribution area
    levinneisyysalue: Mapped[Optional[str]] = mapped_column(String(255))
    # Distribution area detail
    levinneisyysalueen_tarkenne: Mapped[Optional[str]] = mapped_column(String(255))
    # Origin or introduced status
    alkuperainen_vai_tulokas: Mapped[Optional[str]] = mapped_column(String(255))
    # Reference number
    viitenro: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    # Additional information
    lisatietoja: Mapped[Optional[str]] = mapped_column(String(255))
    # Taxon
    taksoni: Mapped['Taksoni'] = relationship('Taksoni', back_populates='maailman_levinneisyysalue')
