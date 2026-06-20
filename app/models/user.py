import enum
from .base import Base, TimestampMixin
from typing import Annotated, Optional
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Enum as SQLEnum, String, Integer


class RoleEnum(str, enum.Enum):
    ADMIN = "admin"
    USER = "user"
    STAFF = "staff"


class User(Base, TimestampMixin):
    __tablename__ = 'users'
    # User ID
    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # Username
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    # Password
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    # Role ID (foreign key to Role table)
    role_name: Mapped[RoleEnum] = mapped_column(SQLEnum(RoleEnum), nullable=False)