from __future__ import annotations

from openapi_spec_validator import validate_spec

from app.main import app


def test_openapi_schema_is_valid():
    spec = app.openapi()
    validate_spec(spec)


def test_openapi_has_all_routes():
    spec = app.openapi()
    paths = spec.get("paths", {})

    for route in app.router.routes:
        methods = getattr(route, "methods", set())
        if not methods:
            continue
        if route.path.startswith("/docs") or route.path.startswith("/redoc") or route.path == "/openapi.json":
            continue
        if not getattr(route, "include_in_schema", True):
            continue

        path_item = paths.get(route.path)
        assert path_item is not None, f"Missing OpenAPI path for {route.path}"
        for method in methods:
            method_key = method.lower()
            assert method_key in path_item, f"Missing OpenAPI method {method} for {route.path}"
