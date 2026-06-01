from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Taksoni(Base):
    # Taxon
    __tablename__ = 'taksoni'
    __searchable_columns__ = ('tieteellinen_nimi', 'suku', 'laji')
    __table_args__ = (ForeignKeyConstraint(['jarjestysnumero'], ['heimo.jarjestysnumero'], name='taksoni_ibfk_1'), ForeignKeyConstraint(['viitenro'], ['viite.viitenro'], name='taksoni_ibfk_2'), Index('IDX_Taksoni1', 'jarjestysnumero'), Index('IDX_Taksoni2', 'viitenro'))
    # Taxon number
    taksonin_nro: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Scientific name
    tieteellinen_nimi: Mapped[str] = mapped_column(String(255), nullable=False, server_default=text("''"))
    # Genus
    suku: Mapped[Optional[str]] = mapped_column(String(255))
    # Genus author
    suvun_auktori: Mapped[Optional[str]] = mapped_column(String(255))
    # Species
    laji: Mapped[Optional[str]] = mapped_column(String(255))
    # Species author
    lajin_auktori: Mapped[Optional[str]] = mapped_column(String(255))
    # Sublevel 1
    alataso_1: Mapped[Optional[str]] = mapped_column(String(255))
    # Sublevel 1 reference
    alatason_1_viite: Mapped[Optional[int]] = mapped_column(Integer)
    # Sublevel 2
    alataso_2: Mapped[Optional[str]] = mapped_column(String(255))
    # Sublevel 2 author
    alatason_2_auktori: Mapped[Optional[str]] = mapped_column(String(255))
    # Sublevel 1 author
    alatason_1_auktori: Mapped[Optional[str]] = mapped_column(String(255))
    # Sublevel 2 reference
    alatason_2_viite: Mapped[Optional[int]] = mapped_column(Integer)
    # Sublevel 3
    alataso_3: Mapped[Optional[str]] = mapped_column(String(255))
    # Sublevel 3 author
    alatason_3_auktori: Mapped[Optional[str]] = mapped_column(String(255))
    # Sublevel 3 reference
    alatason_3_viite: Mapped[Optional[int]] = mapped_column(Integer)
    # Sublevel 4
    alataso_4: Mapped[Optional[str]] = mapped_column(String(255))
    # Sublevel 4 author
    alatason_4_auktori: Mapped[Optional[str]] = mapped_column(String(255))
    # Sublevel 4 reference
    alatason_4_viite: Mapped[Optional[int]] = mapped_column(Integer)
    # Sublevel 5
    alataso_5: Mapped[Optional[str]] = mapped_column(String(255))
    # Sublevel 5 author
    alatason_5_auktori: Mapped[Optional[str]] = mapped_column(String(255))
    # Sublevel 5 reference
    alatason_5_viite: Mapped[Optional[int]] = mapped_column(Integer)
    # Hybrid information
    risteymatiedot: Mapped[Optional[str]] = mapped_column(String(255))
    # Hybrid information author
    risteymatietojen_auktori: Mapped[Optional[str]] = mapped_column(String(255))
    # Last update date
    viimeinen_paivityspvm: Mapped[Optional[str]] = mapped_column(String(255))
    # Additional information
    muita_tietoja: Mapped[Optional[str]] = mapped_column(Text)
    # Order number
    jarjestysnumero: Mapped[Optional[int]] = mapped_column(Integer)
    # Reference number
    viitenro: Mapped[Optional[int]] = mapped_column(Integer)
    # Species reference
    lajin_viite: Mapped[Optional[str]] = mapped_column(String(255))
    # Species reference 2
    lajin_viite2: Mapped[Optional[str]] = mapped_column(String(255))
    # General reference
    yleis_viite: Mapped[Optional[str]] = mapped_column(String(255))
    # Free general reference
    vap_yleis_viite: Mapped[Optional[str]] = mapped_column(String(255))
    # PUT flag
    put: Mapped[Optional[int]] = mapped_column(Integer)
    # PUT value
    puttia: Mapped[Optional[str]] = mapped_column(String(255))
    # Hybrid reference
    risteymaviite: Mapped[Optional[str]] = mapped_column(String(255))
    # Taxonomic family
    heimo: Mapped[Optional['Heimo']] = relationship('Heimo', back_populates='taksoni')
    # Reference or bibliographic citation
    viite: Mapped[Optional['Viite']] = relationship('Viite', back_populates='taksoni')
    # Original growing site
    alkuperainen_kasvupaikka: Mapped[list['AlkuperainenKasvupaikka']] = relationship('AlkuperainenKasvupaikka', back_populates='taksoni')
    # Acquisition data
    hankintatiedot: Mapped[list['Hankintatiedot']] = relationship('Hankintatiedot', back_populates='taksoni')
    # International agreements
    kansainvaliset_sopimukset: Mapped[list['KansainvalisetSopimukset']] = relationship('KansainvalisetSopimukset', back_populates='taksoni')
    # Plant usage purpose
    kasvin_kayttotarkoitus: Mapped[list['KasvinKayttotarkoitus']] = relationship('KasvinKayttotarkoitus', back_populates='taksoni')
    # World distribution area
    maailman_levinneisyysalue: Mapped[list['MaailmanLevinneisyysalue']] = relationship('MaailmanLevinneisyysalue', back_populates='taksoni')
    # Foreign-language name
    muunkielinen_nimi: Mapped[list['MuunkielinenNimi']] = relationship('MuunkielinenNimi', back_populates='taksoni')
    # Specimen data
    naytetieto: Mapped[list['Naytetieto']] = relationship('Naytetieto', back_populates='taksoni')
    # Finnish growing site
    suomalainen_kasvupaikka: Mapped[list['SuomalainenKasvupaikka']] = relationship('SuomalainenKasvupaikka', back_populates='taksoni')
    # Distribution area in Finland
    suomalainen_levinneisyysalue: Mapped[list['SuomalainenLevinneisyysalue']] = relationship('SuomalainenLevinneisyysalue', back_populates='taksoni')
    # Planned growing site
    suunniteltu_kasvupaikka: Mapped[list['SuunniteltuKasvupaikka']] = relationship('SuunniteltuKasvupaikka', back_populates='taksoni')
    # Synonym
    synonyymi: Mapped[list['Synonyymi']] = relationship('Synonyymi', back_populates='taksoni')
    # Taxon label
    taksonin_lappu: Mapped[list['TaksoninLappu']] = relationship('TaksoninLappu', back_populates='taksoni')
    # Taxon cultivation data
    taksonin_viljelytiedot: Mapped[list['TaksoninViljelytiedot']] = relationship('TaksoninViljelytiedot', back_populates='taksoni')
    # Environmental indicator characteristic
    ymparistoindikaattoriluonne: Mapped[list['Ymparistoindikaattoriluonne']] = relationship('Ymparistoindikaattoriluonne', back_populates='taksoni')
