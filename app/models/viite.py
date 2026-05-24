from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Viite(Base):
    # Reference or bibliographic citation
    __tablename__ = 'viite'
    # Reference number
    viitenro: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    # Viitteen Abbreviation
    viitteen_lyhenne: Mapped[Optional[str]] = mapped_column(String(255))
    # Tekija
    tekija: Mapped[Optional[str]] = mapped_column(String(255))
    # Kirjan Name
    kirjan_nimi: Mapped[Optional[str]] = mapped_column(String(255))
    # Kirja Explanation
    kirja_selite: Mapped[Optional[str]] = mapped_column(String(255))
    # Kustantaja
    kustantaja: Mapped[Optional[str]] = mapped_column(String(255))
    # Painos
    painos: Mapped[Optional[str]] = mapped_column(String(255))
    # Year
    vuosi: Mapped[Optional[str]] = mapped_column(String(255))
    # ISBN
    ISBN: Mapped[Optional[str]] = mapped_column(String(255))
    # Location
    sijainti: Mapped[Optional[str]] = mapped_column(String(255))
    # Taxon
    taksoni: Mapped[list['Taksoni']] = relationship('Taksoni', back_populates='viite')
    # Original growing site
    alkuperainen_kasvupaikka: Mapped[list['AlkuperainenKasvupaikka']] = relationship('AlkuperainenKasvupaikka', back_populates='viite')
    # International agreements
    kansainvaliset_sopimukset: Mapped[list['KansainvalisetSopimukset']] = relationship('KansainvalisetSopimukset', back_populates='viite')
    # Plant usage purpose
    kasvin_kayttotarkoitus: Mapped[list['KasvinKayttotarkoitus']] = relationship('KasvinKayttotarkoitus', back_populates='viite')
    # Foreign-language name
    muunkielinen_nimi: Mapped[list['MuunkielinenNimi']] = relationship('MuunkielinenNimi', back_populates='viite')
    # Specimen data
    naytetieto: Mapped[list['Naytetieto']] = relationship('Naytetieto', back_populates='viite')
    # Finnish growing site
    suomalainen_kasvupaikka: Mapped[list['SuomalainenKasvupaikka']] = relationship('SuomalainenKasvupaikka', back_populates='viite')
    # Distribution area in Finland
    suomalainen_levinneisyysalue: Mapped[list['SuomalainenLevinneisyysalue']] = relationship('SuomalainenLevinneisyysalue', back_populates='viite')
    # Synonym
    synonyymi: Mapped[list['Synonyymi']] = relationship('Synonyymi', back_populates='viite')
    # Environmental indicator characteristic
    ymparistoindikaattoriluonne: Mapped[list['Ymparistoindikaattoriluonne']] = relationship('Ymparistoindikaattoriluonne', back_populates='viite')
