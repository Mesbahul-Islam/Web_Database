from .base import Base
from typing import Optional
import datetime
from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, String, Table, Text, text
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Toimenpide(Base):
    # Action
    __tablename__ = 'toimenpide'
    __table_args__ = (ForeignKeyConstraint(['hankintaID'], ['hankintatiedot.hankintaID'], name='toimenpide_ibfk_1'), Index('IDX_Toimenpide1', 'hankintaID'))
    # Action number
    toimenpide_nro: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Date
    pvm: Mapped[Optional[str]] = mapped_column(String(255))
    # Action
    toimenpide: Mapped[Optional[str]] = mapped_column(String(255))
    # Acquisition ID
    hankintaID: Mapped[Optional[int]] = mapped_column(Integer)
    # New date
    uus_pvm: Mapped[Optional[datetime.date]] = mapped_column(Date)
    # Acquisition data
    hankintatiedot: Mapped[Optional['Hankintatiedot']] = relationship('Hankintatiedot', back_populates='toimenpide')
