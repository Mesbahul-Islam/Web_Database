from sqlalchemy import Column, String, Table, Integer
from sqlalchemy.sql import expression
from .base import Base

class ListaTarkastajanimi(Base):
    __table__ = Table(
        "lista_tarkastajanimi",
        Base.metadata,
        Column("id", Integer),
        Column("nimi", String(255)),
        extend_existing=True,
    )
    __mapper_args__ = {"primary_key": [__table__.c.id, __table__.c.nimi]}

