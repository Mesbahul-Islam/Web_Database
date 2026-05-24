from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Hankintatiedot(Base):
    # Acquisition data
    __tablename__ = 'hankintatiedot'
    __table_args__ = (ForeignKeyConstraint(['lahettajanro'], ['lahettaja.lahettajanro'], name='hankintatiedot_ibfk_2'), ForeignKeyConstraint(['taksonin_nro'], ['taksoni.taksonin_nro'], name='hankintatiedot_ibfk_1'), Index('IDX_Hankintatiedot1', 'taksonin_nro'), Index('IDX_Hankintatiedot2', 'lahettajanro'), Index('hankintanumero', 'hankintanumero', unique=True))
    # Acquisition ID
    hankintaID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    # Taxon number
    taksonin_nro: Mapped[int] = mapped_column(INTEGER(11), nullable=False, server_default=text('0'))
    # Sender number
    lahettajanro: Mapped[int] = mapped_column(INTEGER(11), nullable=False, server_default=text('0'))
    # Acquisition number
    hankintanumero: Mapped[Optional[str]] = mapped_column(String(255))
    # Arrival date
    saapumispvm: Mapped[Optional[str]] = mapped_column(String(255))
    # Acquisition name
    hankintanimi: Mapped[Optional[str]] = mapped_column(String(255))
    # Received as
    millaisena_saatu: Mapped[Optional[str]] = mapped_column(String(255))
    # Special collection in own garden
    erikoiskokoelma_oma_puutarha: Mapped[Optional[str]] = mapped_column(String(255))
    # Material value
    materiaalin_arvo: Mapped[Optional[str]] = mapped_column(String(255))
    # Additional information
    lisatiedot: Mapped[Optional[str]] = mapped_column(String(255))
    # Order number
    jarjestysnro: Mapped[Optional[str]] = mapped_column(String(255))
    # Year
    vuosi: Mapped[Optional[str]] = mapped_column(String(255))
    # Addition date
    lisaysPVM: Mapped[Optional[str]] = mapped_column(String(255))
    # Addition history
    lisayshistoria: Mapped[Optional[str]] = mapped_column(Text)
    # Plant remarks
    kasvin_huomautuksia: Mapped[Optional[str]] = mapped_column(Text)
    # Acquisition history
    hankintahistoria: Mapped[Optional[str]] = mapped_column(Text)
    # PUT flag
    put: Mapped[Optional[int]] = mapped_column(TINYINT(1))
    # PUT value
    puttia: Mapped[Optional[str]] = mapped_column(String(255))
    # Number
    numero: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    # Vuosiluku
    vuosiluku: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    # Taxonomic family
    heimo: Mapped[Optional[str]] = mapped_column(String(255))
    # Sender or source
    lahettaja: Mapped['Lahettaja'] = relationship('Lahettaja', back_populates='hankintatiedot')
    # Taxon
    taksoni: Mapped['Taksoni'] = relationship('Taksoni', back_populates='hankintatiedot')
    # Origin-related information
    alkuperaa_koskevat_tiedot: Mapped[list['AlkuperaaKoskevatTiedot']] = relationship('AlkuperaaKoskevatTiedot', back_populates='hankintatiedot')
    # Cultivation records
    kasvatustietoja: Mapped[list['Kasvatustietoja']] = relationship('Kasvatustietoja', back_populates='hankintatiedot')
    # Identification mark record
    maaritysmerkinta: Mapped[list['Maaritysmerkinta']] = relationship('Maaritysmerkinta', back_populates='hankintatiedot')
    # Specimen information
    naytetietoja: Mapped[list['Naytetietoja']] = relationship('Naytetietoja', back_populates='hankintatiedot')
    # Section location
    osastopaikka: Mapped[list['Osastopaikka']] = relationship('Osastopaikka', back_populates='hankintatiedot')
    # Garden cultivation purpose
    puutarhassa_viljelyn_tarkoitus: Mapped[list['PuutarhassaViljelynTarkoitus']] = relationship('PuutarhassaViljelynTarkoitus', back_populates='hankintatiedot')
    # Action
    toimenpide: Mapped[list['Toimenpide']] = relationship('Toimenpide', back_populates='hankintatiedot')
