from .base import Base, TimestampMixin
from typing import Optional
import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Kasvatustietoja(Base, TimestampMixin):
    # Cultivation records
    __tablename__ = 'kasvatustietoja'
    __table_args__ = (ForeignKeyConstraint(['hankintaID'], ['hankintatiedot.hankintaID'], name='kasvatustietoja_ibfk_1'), Index('IDX_Kasvatustietoja1', 'hankintaID'))
    # Cultivation additional information number
    lisatietojen_nro_kasvatus: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Acquisition ID
    hankintaID: Mapped[int] = mapped_column(Integer, nullable=False, server_default=text('0'))
    # Seed bank
    siemenpankki: Mapped[Optional[str]] = mapped_column(String(255))
    # Seeds remaining
    siemenia_jaljella: Mapped[Optional[str]] = mapped_column(String(255))
    # Seed storage method
    siementen_varastoimistapa: Mapped[Optional[str]] = mapped_column(String(255))
    # Research
    tutkimus: Mapped[Optional[str]] = mapped_column(String(255))
    # Remarks
    huomautuksia: Mapped[Optional[str]] = mapped_column(Text)
    # Date
    pvm: Mapped[Optional[str]] = mapped_column(String(100))
    # Acquisition data
    hankintatiedot: Mapped['Hankintatiedot'] = relationship('Hankintatiedot', back_populates='kasvatustietoja')
