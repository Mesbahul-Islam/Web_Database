from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class TaksoninViljelytiedot(Base):
    # Taxon cultivation data
    __tablename__ = 'taksonin_viljelytiedot'
    __table_args__ = (ForeignKeyConstraint(['taksonin_nro'], ['taksoni.taksonin_nro'], name='taksonin_viljelytiedot_ibfk_1'), Index('IDX_Taksonin_viljelytiedot1', 'taksonin_nro'))
    # Cultivation additional information number
    lisatietojen_nro_viljely: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    # Taxon number
    taksonin_nro: Mapped[int] = mapped_column(INTEGER(11), nullable=False, server_default=text('0'))
    # Plant diseases and pests
    kasvitaudit_ja_tuholaiset: Mapped[Optional[str]] = mapped_column(String(255))
    # Tolerates following pesticides
    kestaa_seuraavia_torjuntaaineita: Mapped[Optional[str]] = mapped_column(String(255))
    # Does not tolerate following pesticides
    ei_kesta_seuraavia_torjunta_aineita: Mapped[Optional[str]] = mapped_column(String(255))
    # Special growing medium requirements
    erityisia_kasvualustavaatimuksia: Mapped[Optional[str]] = mapped_column(String(255))
    # Special light requirements
    erityisia_valovaatimuksia: Mapped[Optional[str]] = mapped_column(String(255))
    # Special temperature or overwintering requirements
    erityisia_lampotila_tai_talvehtimisvaatimuksia: Mapped[Optional[str]] = mapped_column(String(255))
    # Propagation method
    lisaystapa: Mapped[Optional[str]] = mapped_column(String(255))
    # Seed collection
    siementen_keruu: Mapped[Optional[str]] = mapped_column(String(255))
    # Seed storage
    siementen_sailytys: Mapped[Optional[str]] = mapped_column(String(255))
    # Tuulenkestavyys
    tuulenkestavyys: Mapped[Optional[str]] = mapped_column(String(255))
    # Climatic hardiness
    ilmastollinen_kestavyys: Mapped[Optional[str]] = mapped_column(String(255))
    # Climatic hardiness of cultivated plants
    viljelykasvien_ilmastollinen_kestavyys: Mapped[Optional[str]] = mapped_column(String(255))
    # Stem or trunk
    varsi: Mapped[Optional[str]] = mapped_column(String(255))
    # Growth form
    kasvumuoto: Mapped[Optional[str]] = mapped_column(String(255))
    # Growth habit
    kasvutapa: Mapped[Optional[str]] = mapped_column(String(255))
    # Elevation
    korkeus: Mapped[Optional[str]] = mapped_column(String(255))
    # Pollination method
    polytystapa: Mapped[Optional[str]] = mapped_column(String(255))
    # Advice and domesticity
    neuvoisuus_ja_kotisuus: Mapped[Optional[str]] = mapped_column(String(255))
    # Muita viljelytietoja
    muita_viljelytietoja: Mapped[Optional[str]] = mapped_column(Text)
    # Protected status
    rauhoitus: Mapped[Optional[str]] = mapped_column(String(255))
    # Threat category in Finland
    uhanalaisuusluokka_suomessa: Mapped[Optional[str]] = mapped_column(String(255))
    # Threat category worldwide
    uhanalaisuusluokka_maailmalla: Mapped[Optional[str]] = mapped_column(String(255))
    # Muita ominaisuuksia
    muita_ominaisuuksia: Mapped[Optional[str]] = mapped_column(Text)
    # Harmfulness
    haitallisuus: Mapped[Optional[str]] = mapped_column(String(255))
    # Toxicity
    myrkyllisyys: Mapped[Optional[str]] = mapped_column(String(255))
    # Agreements
    sopimukset: Mapped[Optional[str]] = mapped_column(String(255))
    # Free reference
    vapaa_viite: Mapped[Optional[str]] = mapped_column(String(255))
    # Taxon
    taksoni: Mapped['Taksoni'] = relationship('Taksoni', back_populates='taksonin_viljelytiedot')
