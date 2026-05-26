import enum
from .base import Base
from typing import Annotated
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Enum as SQLEnum, String, Integer


class RoleEnum(str, enum.Enum):
    ADMIN = "admin"
    USER = "user"
    STAFF = "staff"


class User(Base):
    __tablename__ = 'users'
    # User ID
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Username
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    # Password
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    # Role ID (foreign key to Role table)
    role_name: Mapped[RoleEnum] = mapped_column(SQLEnum(RoleEnum), nullable=False)