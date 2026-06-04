from __future__ import annotations

from pathlib import Path
import sys

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.database import get_db
from app.main import app


class _FakeQuery:
    def options(self, *args, **kwargs):
        return self

    def filter(self, *args, **kwargs):
        return self

    def offset(self, *args, **kwargs):
        return self

    def limit(self, *args, **kwargs):
        return self

    def count(self):
        return 0

    def all(self):
        return []

    def first(self):
        return None


class _FakeSession:
    def query(self, *args, **kwargs):
        return _FakeQuery()


def _override_get_db():
    yield _FakeSession()


def test_read_one_routes_use_valid_model_fields():
    app.dependency_overrides[get_db] = _override_get_db
    client = TestClient(app, raise_server_exceptions=False)
    failures = []

    for route in app.router.routes:
        methods = getattr(route, "methods", set())
        if "GET" not in methods:
            continue
        if "{" not in route.path:
            continue

        path = route.path
        for param in route.dependant.path_params:
            path = path.replace(f"{{{param.name}}}", "0")

        response = client.get(path)
        if response.status_code == 500:
            failures.append(path)
            continue
        assert response.status_code in {200, 404, 422}

    app.dependency_overrides.clear()
    assert not failures, f"Internal errors for routes: {', '.join(sorted(failures))}"
