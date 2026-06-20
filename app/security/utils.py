import jwt
from datetime import datetime, timezone
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from app.core.oauth_client import oauth2_scheme
from app.database import get_db
from app.models.user import User
from app.schemas.token import TokenData
from app.security.token import password_hash
from app.core.config import settings
from jwt.exceptions import InvalidTokenError
from app.security.token import DUMMY_HASH


def get_user(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username == username).first()


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(get_db)],
):
    credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        exp = payload.get("exp")
        if exp is not None and datetime.fromtimestamp(exp, tz=timezone.utc) < datetime.now(timezone.utc):
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


def verify_password(plain_password, hashed_password):
    try:
        return password_hash.verify(plain_password, hashed_password)
    except Exception:
        return False


def get_password_hash(password):
    return password_hash.hash(password)

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False
    if not verify_password(password, user.password):
        return False
    return user

