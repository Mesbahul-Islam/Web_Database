from .base import Base, TimestampMixin
from typing import Optional
import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Lahettaja(Base, TimestampMixin):
    # Sender or source
    __tablename__ = 'lahettaja'
    # Sender number
    lahettajanro: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Sender type
    lahettajatyyppi: Mapped[Optional[str]] = mapped_column(String(255))
    # Sender identifier in the garden
    lahettajan_tunnus_puutarha: Mapped[Optional[str]] = mapped_column(String(255))
    # International sender identifier
    lahettajan_tunnus_kansainvalinen: Mapped[Optional[str]] = mapped_column(String(255))
    # Sender name
    lahettajan_nimi: Mapped[Optional[str]] = mapped_column(String(255))
    # Street address
    lahiosoite: Mapped[Optional[str]] = mapped_column(String(255))
    # Post office box
    postilokero: Mapped[Optional[str]] = mapped_column(String(255))
    # Postal code
    postinumero: Mapped[Optional[str]] = mapped_column(String(255))
    # Post office city
    postitoimipaikka: Mapped[Optional[str]] = mapped_column(String(255))
    # City
    kaupunki: Mapped[Optional[str]] = mapped_column(String(255))
    # State
    osavaltio: Mapped[Optional[str]] = mapped_column(String(255))
    # Country
    maa: Mapped[Optional[str]] = mapped_column(String(255))
    # Contact person
    kontaktihenkilo: Mapped[Optional[str]] = mapped_column(String(255))
    # Email
    e_mail: Mapped[Optional[str]] = mapped_column(String(255))
    # Website
    web_sivut: Mapped[Optional[str]] = mapped_column(String(255))
    # Address registration date
    osoitteen_kirjauspvm: Mapped[Optional[str]] = mapped_column(String(255))
    # Rio agreement
    Rion_sopimus: Mapped[Optional[str]] = mapped_column(String(255))
    # Sender additional information
    lahettajan_lisatiedot: Mapped[Optional[str]] = mapped_column(String(255))
    # Search name
    hakunimi: Mapped[Optional[str]] = mapped_column(String(255))
    # Acquisition data
    hankintatiedot: Mapped[list['Hankintatiedot']] = relationship('Hankintatiedot', back_populates='lahettaja')
