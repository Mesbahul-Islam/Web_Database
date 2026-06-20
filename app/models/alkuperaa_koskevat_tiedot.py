from .base import Base, TimestampMixin
from typing import Optional
import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class AlkuperaaKoskevatTiedot(Base, TimestampMixin):
    # Origin-related information
    __tablename__ = 'alkuperaa_koskevat_tiedot'
    __table_args__ = (ForeignKeyConstraint(['hankintaID'], ['hankintatiedot.hankintaID'], name='alkuperaa_koskevat_tiedot_ibfk_1'), Index('IDX_Alkuperaa_koskevat_tiedot1', 'hankintaID'))
    # Origin number
    alkupera_nro: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Acquisition ID
    hankintaID: Mapped[int] = mapped_column(Integer, nullable=False, server_default=text('0'))
    # Origin type
    alkuperatyyppi: Mapped[Optional[str]] = mapped_column(String(255))
    # Country
    maa: Mapped[Optional[str]] = mapped_column(String(255))
    # Country ISO code
    maan_ISOkoodi: Mapped[Optional[str]] = mapped_column(String(255))
    # Area
    alue: Mapped[Optional[str]] = mapped_column(String(255))
    # Sub-area
    ala_alue: Mapped[Optional[str]] = mapped_column(String(255))
    # Municipality
    kunta: Mapped[Optional[str]] = mapped_column(String(255))
    # Village
    kyla: Mapped[Optional[str]] = mapped_column(String(255))
    # Latitude
    latitude: Mapped[Optional[str]] = mapped_column(String(255))
    # Longitude
    longitude: Mapped[Optional[str]] = mapped_column(String(255))
    # Grid 27 E
    grid_27_E: Mapped[Optional[str]] = mapped_column(String(255))
    # Growing site
    kasvupaikka: Mapped[Optional[str]] = mapped_column(String(255))
    # Elevation
    korkeus: Mapped[Optional[str]] = mapped_column(String(255))
    # Collector
    keraaja: Mapped[Optional[str]] = mapped_column(String(255))
    # Collection date
    kerayspvm: Mapped[Optional[str]] = mapped_column(String(255))
    # Collection number
    keraysnumero: Mapped[Optional[str]] = mapped_column(String(255))
    # Other collection information
    muita_keraystietoja: Mapped[Optional[str]] = mapped_column(Text)
    # Collection trip
    keraysretki: Mapped[Optional[str]] = mapped_column(String(255))
    # Acquisition data
    hankintatiedot: Mapped['Hankintatiedot'] = relationship('Hankintatiedot', back_populates='alkuperaa_koskevat_tiedot')
