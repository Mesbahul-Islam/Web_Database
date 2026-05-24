from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class SuomalainenKasvupaikka(Base):
    # Finnish growing site
    __tablename__ = 'suomalainen_kasvupaikka'
    __table_args__ = (ForeignKeyConstraint(['taksonin_nro'], ['taksoni.taksonin_nro'], name='suomalainen_kasvupaikka_ibfk_1'), ForeignKeyConstraint(['viitenro'], ['viite.viitenro'], name='suomalainen_kasvupaikka_ibfk_2'), Index('IDX_Suomalainen_kasvupaikka1', 'taksonin_nro'), Index('IDX_Suomalainen_kasvupaikka2', 'viitenro'))
    # Finnish growing site number
    suomalaisen_kasvupaikan_nro: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    # Taxon number
    taksonin_nro: Mapped[int] = mapped_column(INTEGER(11), nullable=False, server_default=text('0'))
    # Growing site
    kasvupaikka: Mapped[Optional[str]] = mapped_column(String(255))
    # Growing site type
    kasvupaikan_tyyppi: Mapped[Optional[str]] = mapped_column(String(255))
    # Reference number
    viitenro: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    # Taxon
    taksoni: Mapped['Taksoni'] = relationship('Taksoni', back_populates='suomalainen_kasvupaikka')
    # Reference or bibliographic citation
    viite: Mapped[Optional['Viite']] = relationship('Viite', back_populates='suomalainen_kasvupaikka')
