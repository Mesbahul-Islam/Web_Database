from __future__ import annotations

from pathlib import Path
import sys
from datetime import timedelta

import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.database import get_db
from app.main import app
from app.models.user import User, RoleEnum
from app.security.token import create_access_token
from app.security.utils import get_password_hash


@pytest.fixture()
def client(db_session):
    def _override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = _override_get_db
    try:
        yield TestClient(app)
    finally:
        app.dependency_overrides.clear()


@pytest.fixture()
def seeded_user(db_session):
    user = User(
        username="auth-test-user",
        password=get_password_hash("secret-password"),
        role_name=RoleEnum.USER,
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    yield user
    db_session.delete(user)
    db_session.commit()


def test_login_returns_bearer_token(client, seeded_user):
    response = client.post(
        "/auth/token",
        data={"username": seeded_user.username, "password": "secret-password"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["token_type"] == "bearer"
    assert isinstance(payload["access_token"], str)
    assert payload["access_token"]


def test_login_rejects_invalid_password(client, seeded_user):
    response = client.post(
        "/auth/token",
        data={"username": seeded_user.username, "password": "wrong-password"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid authentication credentials"


def test_users_me_requires_valid_bearer_token(client, seeded_user):
    login_response = client.post(
        "/auth/token",
        data={"username": seeded_user.username, "password": "secret-password"},
    )
    token = login_response.json()["access_token"]

    response = client.get(
        "/auth/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["username"] == seeded_user.username
    assert body["role_name"] == seeded_user.role_name.value


def test_users_me_rejects_missing_token(client):
    response = client.get("/auth/users/me")

    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"


def test_users_me_rejects_expired_token(client, seeded_user):
    expired_token = create_access_token(
        data={"sub": seeded_user.username},
        expires_delta=timedelta(seconds=-1),
    )

    response = client.get(
        "/auth/users/me",
        headers={"Authorization": f"Bearer {expired_token}"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"