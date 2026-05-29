from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Heimo(Base):
    # Taxonomic family
    __tablename__ = 'heimo'
    # Order number
    jarjestysnumero: Mapped[int] = mapped_column(Integer, primary_key=True, server_default=text('0'))
    # Name
    nimi: Mapped[Optional[str]] = mapped_column(String(255))
    # Synonym
    synonyymi: Mapped[Optional[str]] = mapped_column(String(255))
    # Number
    numero: Mapped[Optional[str]] = mapped_column(String(255))
    # Order
    lahko: Mapped[Optional[str]] = mapped_column(String(255))
    # Order number
    lahkonnumero: Mapped[Optional[str]] = mapped_column(String(255))
    # Subclass
    alaluokka: Mapped[Optional[str]] = mapped_column(String(255))
    # Subclass number
    alaluokannumero: Mapped[Optional[str]] = mapped_column(String(255))
    # Class
    luokka: Mapped[Optional[str]] = mapped_column(String(255))
    # Class number
    luokannumero: Mapped[Optional[str]] = mapped_column(String(255))
    # Main group
    paaryhma: Mapped[Optional[str]] = mapped_column(String(255))
    # Main group number
    paaryhmannumero: Mapped[Optional[str]] = mapped_column(String(255))
    # Finnish name
    suom_nimi: Mapped[Optional[str]] = mapped_column(String(255))
    # Taxon
    taksoni: Mapped[list['Taksoni']] = relationship('Taksoni', back_populates='heimo')
