from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class SuunniteltuKasvupaikka(Base):
    # Planned growing site
    __tablename__ = 'suunniteltu_kasvupaikka'
    __table_args__ = (ForeignKeyConstraint(['taksonin_nro'], ['taksoni.taksonin_nro'], name='suunniteltu_kasvupaikka_ibfk_1'), Index('IDX_Suunniteltu_kasvupaikka1', 'taksonin_nro'))
    # Growing site number
    kasvupaikan_nro: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Taxon number
    taksonin_nro: Mapped[int] = mapped_column(Integer, nullable=False, server_default=text('0'))
    # Section
    osasto: Mapped[Optional[str]] = mapped_column(String(255))
    # Placement location
    sijoituspaikka: Mapped[Optional[str]] = mapped_column(String(255))
    # Taxon
    taksoni: Mapped['Taksoni'] = relationship('Taksoni', back_populates='suunniteltu_kasvupaikka')
