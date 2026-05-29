from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class PuutarhassaViljelynTarkoitus(Base):
    # Garden cultivation purpose
    __tablename__ = 'puutarhassa_viljelyn_tarkoitus'
    __table_args__ = (ForeignKeyConstraint(['hankintaID'], ['hankintatiedot.hankintaID'], name='puutarhassa_viljelyn_tarkoitus_ibfk_1'), Index('IDX_Puutarhassa_viljelyn_tarkoitus1', 'hankintaID'))
    # Viljely number
    viljely_nro: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Acquisition ID
    hankintaID: Mapped[int] = mapped_column(Integer, nullable=False, server_default=text('0'))
    # Garden cultivation purpose
    puutarhassa_viljelyn_tarkoitus: Mapped[Optional[str]] = mapped_column(String(255))
    # In the garden cultivation detail
    puutarhassa_viljelyn_tarkenne: Mapped[Optional[str]] = mapped_column(String(255))
    # Acquisition data
    hankintatiedot: Mapped['Hankintatiedot'] = relationship('Hankintatiedot', back_populates='puutarhassa_viljelyn_tarkoitus')
