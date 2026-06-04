"""
End-to-end tests: pagination, column filtering, full-text search, nested FK routes,
and OpenAPI documentation of filter params.
"""
from __future__ import annotations

import importlib
from math import ceil

import pytest

from app.models.taksoni import Taksoni
from app.models.hankintatiedot import Hankintatiedot
from app.models.alkuperaa_koskevat_tiedot import AlkuperaaKoskevatTiedot
from app.models.synonyymi import Synonyymi
from app.models.heimo import Heimo
from app.models.sijoituspaikka import Sijoituspaikka
from app.models.tarkastusmerkinta import Tarkastusmerkinta

PAGE_FIELDS = {"items", "total", "page", "page_size", "pages"}


def _is_page_envelope(body: dict) -> bool:
    return isinstance(body, dict) and PAGE_FIELDS <= body.keys()


# ─── helpers ──────────────────────────────────────────────────────────────────

def _get_module_model(route):
    module = importlib.import_module(route.endpoint.__module__)
    return getattr(module, "Model", None)


# ═══════════════════════════════════════════════════════════════════════════════
# 1. LIST ENDPOINT SHAPE
# ═══════════════════════════════════════════════════════════════════════════════

class TestListEndpointShape:
    """Every paginated GET / endpoint must return a SchemaPage envelope."""

    def test_all_list_endpoints_return_200(self, client):
        for route in client.app.router.routes:
            if "GET" not in getattr(route, "methods", set()):
                continue
            if "{" in route.path:
                continue
            if route.path in {
                "/openapi.json", "/docs", "/redoc",
                "/docs/oauth2-redirect", "/cache-stats",
            } or route.path.startswith("/auth/"):
                continue

            r = client.get(route.path, params={"page": 1, "page_size": 1})
            assert r.status_code == 200, f"GET {route.path} → {r.status_code}: {r.text[:200]}"

    def test_paginated_endpoints_return_page_envelope(self, client):
        for route in client.app.router.routes:
            if "GET" not in getattr(route, "methods", set()):
                continue
            if "{" in route.path:
                continue

            model = _get_module_model(route)
            if model is None:
                continue

            r = client.get(route.path, params={"page": 1, "page_size": 1})
            if r.status_code != 200:
                continue

            body = r.json()
            if not isinstance(body, dict):
                continue  # some endpoints still return list (e.g. lahettaja)

            if "items" in body:
                assert _is_page_envelope(body), (
                    f"GET {route.path} has 'items' but is missing fields: "
                    f"{PAGE_FIELDS - body.keys()}"
                )
                assert isinstance(body["items"], list)
                assert isinstance(body["total"], int) and body["total"] >= 0
                assert isinstance(body["page"], int) and body["page"] >= 1
                assert isinstance(body["page_size"], int) and body["page_size"] >= 1
                assert isinstance(body["pages"], int) and body["pages"] >= 0

    def test_taksoni_list_returns_page_envelope(self, client):
        body = client.get("/taksoni/", params={"page": 1, "page_size": 5}).json()
        assert _is_page_envelope(body)
        assert len(body["items"]) == 5

    def test_heimo_list_returns_page_envelope(self, client):
        body = client.get("/heimo/", params={"page": 1, "page_size": 3}).json()
        assert _is_page_envelope(body)

    def test_hankintatiedot_list_returns_page_envelope(self, client):
        body = client.get("/hankintatiedot/", params={"page": 1, "page_size": 5}).json()
        assert _is_page_envelope(body)


# ═══════════════════════════════════════════════════════════════════════════════
# 2. PAGINATION MECHANICS
# ═══════════════════════════════════════════════════════════════════════════════

class TestPagination:

    def test_default_page_is_1(self, client):
        body = client.get("/taksoni/", params={"page_size": 5}).json()
        assert body["page"] == 1

    def test_page_size_controls_item_count(self, client):
        body5 = client.get("/taksoni/", params={"page": 1, "page_size": 5}).json()
        body10 = client.get("/taksoni/", params={"page": 1, "page_size": 10}).json()
        assert len(body5["items"]) == 5
        assert len(body10["items"]) == 10

    def test_page_2_has_different_items_from_page_1(self, client):
        ids1 = {i["taksonin_nro"] for i in
                client.get("/taksoni/", params={"page": 1, "page_size": 5}).json()["items"]}
        ids2 = {i["taksonin_nro"] for i in
                client.get("/taksoni/", params={"page": 2, "page_size": 5}).json()["items"]}
        assert ids1.isdisjoint(ids2), "Page 1 and page 2 share items"

    def test_pages_field_equals_ceil_total_over_page_size(self, client):
        body = client.get("/taksoni/", params={"page": 1, "page_size": 7}).json()
        expected = ceil(body["total"] / 7) if body["total"] else 0
        assert body["pages"] == expected

    def test_total_is_same_on_every_page(self, client):
        t1 = client.get("/taksoni/", params={"page": 1, "page_size": 5}).json()["total"]
        t2 = client.get("/taksoni/", params={"page": 2, "page_size": 5}).json()["total"]
        t3 = client.get("/taksoni/", params={"page": 3, "page_size": 5}).json()["total"]
        assert t1 == t2 == t3

    def test_page_beyond_last_returns_empty_items(self, client):
        total = client.get("/taksoni/", params={"page": 1, "page_size": 1}).json()["total"]
        body = client.get("/taksoni/", params={"page": total + 100, "page_size": 1}).json()
        assert body["items"] == []
        assert body["total"] == total  # total unchanged

    def test_page_size_1_returns_exactly_one_item(self, client):
        body = client.get("/taksoni/", params={"page": 1, "page_size": 1}).json()
        assert len(body["items"]) == 1

    def test_last_page_may_have_fewer_items_than_page_size(self, client):
        total = client.get("/taksoni/", params={"page": 1, "page_size": 1}).json()["total"]
        page_size = 7
        last_page = ceil(total / page_size)
        body = client.get("/taksoni/", params={"page": last_page, "page_size": page_size}).json()
        expected_count = total - (last_page - 1) * page_size
        assert len(body["items"]) == expected_count

    def test_page_less_than_1_returns_422(self, client):
        assert client.get("/taksoni/", params={"page": 0}).status_code == 422

    def test_page_size_less_than_1_returns_422(self, client):
        assert client.get("/taksoni/", params={"page_size": 0}).status_code == 422

    def test_response_echoes_back_requested_page_and_page_size(self, client):
        body = client.get("/taksoni/", params={"page": 3, "page_size": 7}).json()
        assert body["page"] == 3
        assert body["page_size"] == 7

    def test_different_page_sizes_cover_same_total(self, client):
        """Summing all pages with page_size=3 must equal total."""
        total = client.get("/taksoni/", params={"page": 1, "page_size": 1}).json()["total"]
        page_size = 3
        pages = ceil(total / page_size) if total else 0
        collected = 0
        for p in range(1, pages + 1):
            items = client.get("/taksoni/", params={"page": p, "page_size": page_size}).json()["items"]
            collected += len(items)
        assert collected == total


# ═══════════════════════════════════════════════════════════════════════════════
# 3. COLUMN FILTERING
# ═══════════════════════════════════════════════════════════════════════════════

class TestColumnFiltering:

    def test_filter_by_integer_fk_returns_only_matching_rows(self, client, db_session):
        row = db_session.query(AlkuperaaKoskevatTiedot).filter(
            AlkuperaaKoskevatTiedot.hankintaID.isnot(None)
        ).first()
        if not row:
            pytest.skip("No data")

        body = client.get(
            "/alkuperaa_koskevat_tiedot/",
            params={"page": 1, "page_size": 200, "hankintaID": row.hankintaID},
        ).json()

        assert body["total"] > 0
        for item in body["items"]:
            assert item["hankintaID"] == row.hankintaID

    def test_filter_by_string_column_returns_only_matching_rows(self, client, db_session):
        row = db_session.query(Taksoni).filter(Taksoni.suku.isnot(None)).first()
        if not row:
            pytest.skip("No data")

        body = client.get(
            "/taksoni/",
            params={"page": 1, "page_size": 200, "suku": row.suku},
        ).json()

        assert body["total"] > 0
        for item in body["items"]:
            assert item["suku"] == row.suku

    def test_filter_narrows_results_vs_unfiltered(self, client, db_session):
        row = db_session.query(AlkuperaaKoskevatTiedot).first()
        if not row:
            pytest.skip("No data")

        unfiltered = client.get(
            "/alkuperaa_koskevat_tiedot/", params={"page": 1, "page_size": 1}
        ).json()["total"]
        filtered = client.get(
            "/alkuperaa_koskevat_tiedot/",
            params={"page": 1, "page_size": 1, "hankintaID": row.hankintaID},
        ).json()["total"]

        assert filtered <= unfiltered

    def test_unknown_column_filter_is_silently_ignored(self, client):
        r = client.get("/taksoni/", params={"page": 1, "page_size": 5, "does_not_exist": "abc"})
        assert r.status_code == 200
        assert _is_page_envelope(r.json())

    def test_filter_with_no_matching_rows_returns_zero_total(self, client):
        body = client.get(
            "/taksoni/", params={"page": 1, "page_size": 10, "taksonin_nro": -99999}
        ).json()
        assert body["total"] == 0
        assert body["items"] == []

    def test_multiple_filters_are_combined_as_and(self, client, db_session):
        row = db_session.query(Taksoni).filter(
            Taksoni.suku.isnot(None),
            Taksoni.laji.isnot(None),
        ).first()
        if not row:
            pytest.skip("No data")

        body = client.get(
            "/taksoni/",
            params={"page": 1, "page_size": 200, "suku": row.suku, "laji": row.laji},
        ).json()

        for item in body["items"]:
            assert item["suku"] == row.suku
            assert item["laji"] == row.laji

    def test_filter_is_paginated(self, client, db_session):
        """Filtered results still respect page/page_size."""
        row = db_session.query(AlkuperaaKoskevatTiedot).filter(
            AlkuperaaKoskevatTiedot.hankintaID.isnot(None)
        ).first()
        if not row:
            pytest.skip("No data")

        body_all = client.get(
            "/alkuperaa_koskevat_tiedot/",
            params={"page": 1, "page_size": 1000, "hankintaID": row.hankintaID},
        ).json()
        total = body_all["total"]
        if total <= 1:
            pytest.skip("Need >1 matching rows to test pagination of filters")

        body_p1 = client.get(
            "/alkuperaa_koskevat_tiedot/",
            params={"page": 1, "page_size": 1, "hankintaID": row.hankintaID},
        ).json()
        body_p2 = client.get(
            "/alkuperaa_koskevat_tiedot/",
            params={"page": 2, "page_size": 1, "hankintaID": row.hankintaID},
        ).json()

        assert body_p1["total"] == total
        ids1 = {i["alkupera_nro"] for i in body_p1["items"]}
        ids2 = {i["alkupera_nro"] for i in body_p2["items"]}
        assert ids1.isdisjoint(ids2)


# ═══════════════════════════════════════════════════════════════════════════════
# 4. FULL-TEXT SEARCH
# ═══════════════════════════════════════════════════════════════════════════════

class TestSearch:

    def test_search_returns_results(self, client, db_session):
        row = db_session.query(Taksoni).filter(Taksoni.tieteellinen_nimi.isnot(None)).first()
        if not row:
            pytest.skip("No data")

        term = row.tieteellinen_nimi[:5]
        body = client.get("/taksoni/", params={"page": 1, "page_size": 50, "search": term}).json()
        assert body["total"] > 0

    def test_search_results_contain_term_in_a_string_field(self, client, db_session):
        row = db_session.query(Taksoni).filter(Taksoni.tieteellinen_nimi.isnot(None)).first()
        if not row:
            pytest.skip("No data")

        term = row.tieteellinen_nimi[:5].lower()
        body = client.get("/taksoni/", params={"page": 1, "page_size": 50, "search": term}).json()

        for item in body["items"]:
            string_vals = [str(v).lower() for v in item.values() if isinstance(v, str) and v]
            assert any(term in v for v in string_vals), (
                f"Term '{term}' not found in any string field of {item}"
            )

    def test_search_is_case_insensitive(self, client, db_session):
        row = db_session.query(Taksoni).filter(Taksoni.tieteellinen_nimi.isnot(None)).first()
        if not row:
            pytest.skip("No data")

        term = row.tieteellinen_nimi[:5]
        lower = client.get("/taksoni/", params={"page": 1, "page_size": 1, "search": term.lower()}).json()["total"]
        upper = client.get("/taksoni/", params={"page": 1, "page_size": 1, "search": term.upper()}).json()["total"]
        assert lower == upper

    def test_search_reduces_result_count(self, client, db_session):
        row = db_session.query(Taksoni).filter(Taksoni.tieteellinen_nimi.isnot(None)).first()
        if not row:
            pytest.skip("No data")

        total_all = client.get("/taksoni/", params={"page": 1, "page_size": 1}).json()["total"]
        total_search = client.get(
            "/taksoni/", params={"page": 1, "page_size": 1, "search": row.tieteellinen_nimi[:5]}
        ).json()["total"]
        assert total_search <= total_all

    def test_empty_search_returns_same_as_no_search(self, client):
        no_search = client.get("/taksoni/", params={"page": 1, "page_size": 1}).json()["total"]
        empty_search = client.get(
            "/taksoni/", params={"page": 1, "page_size": 1, "search": ""}
        ).json()["total"]
        assert no_search == empty_search

    def test_search_and_column_filter_combine(self, client, db_session):
        row = db_session.query(Taksoni).filter(
            Taksoni.suku.isnot(None),
            Taksoni.tieteellinen_nimi.isnot(None),
        ).first()
        if not row:
            pytest.skip("No data")

        body = client.get(
            "/taksoni/",
            params={"page": 1, "page_size": 200, "suku": row.suku, "search": row.suku[:3]},
        ).json()
        for item in body["items"]:
            assert item["suku"] == row.suku

    def test_nonsense_search_returns_empty(self, client):
        body = client.get(
            "/taksoni/", params={"page": 1, "page_size": 10, "search": "xyzzy_not_a_real_name_12345"}
        ).json()
        assert body["total"] == 0
        assert body["items"] == []


# ═══════════════════════════════════════════════════════════════════════════════
# 5. NESTED FK ROUTES
# ═══════════════════════════════════════════════════════════════════════════════

class TestNestedFKRoutes:

    def test_nested_route_returns_page_envelope(self, client, db_session):
        hankinta = db_session.query(Hankintatiedot).first()
        if not hankinta:
            pytest.skip("No hankintatiedot data")

        r = client.get(f"/hankintatiedot/{hankinta.hankintaID}/alkuperaa_koskevat_tiedot")
        assert r.status_code == 200
        assert _is_page_envelope(r.json())

    def test_nested_route_filters_by_parent_pk(self, client, db_session):
        hankinta = (
            db_session.query(Hankintatiedot)
            .join(AlkuperaaKoskevatTiedot,
                  Hankintatiedot.hankintaID == AlkuperaaKoskevatTiedot.hankintaID)
            .first()
        )
        if not hankinta:
            pytest.skip("No hankintatiedot with alkuperaa_koskevat_tiedot")

        body = client.get(
            f"/hankintatiedot/{hankinta.hankintaID}/alkuperaa_koskevat_tiedot",
            params={"page": 1, "page_size": 200},
        ).json()

        assert body["total"] > 0
        for item in body["items"]:
            assert item["hankintaID"] == hankinta.hankintaID

    def test_nested_route_taksoni_synonyymi(self, client, db_session):
        taksoni = (
            db_session.query(Taksoni)
            .join(Synonyymi, Taksoni.taksonin_nro == Synonyymi.taksonin_nro)
            .first()
        )
        if not taksoni:
            pytest.skip("No taksoni with synonyymi")

        body = client.get(
            f"/taksoni/{taksoni.taksonin_nro}/synonyymi",
            params={"page": 1, "page_size": 200},
        ).json()

        assert body["total"] > 0
        for item in body["items"]:
            assert item["taksonin_nro"] == taksoni.taksonin_nro

    def test_nested_route_heimo_taksoni(self, client, db_session):
        heimo = (
            db_session.query(Heimo)
            .join(Taksoni, Heimo.jarjestysnumero == Taksoni.jarjestysnumero)
            .first()
        )
        if not heimo:
            pytest.skip("No heimo with taksoni")

        body = client.get(
            f"/heimo/{heimo.jarjestysnumero}/taksoni",
            params={"page": 1, "page_size": 10},
        ).json()

        assert body["total"] > 0
        for item in body["items"]:
            assert item["jarjestysnumero"] == heimo.jarjestysnumero

    def test_nested_route_sijoituspaikka_tarkastusmerkinta(self, client, db_session):
        sijoitus = (
            db_session.query(Sijoituspaikka)
            .join(Tarkastusmerkinta,
                  Sijoituspaikka.sijoituspaikan_nro == Tarkastusmerkinta.sijoituspaikan_nro)
            .first()
        )
        if not sijoitus:
            pytest.skip("No sijoituspaikka with tarkastusmerkinta")

        body = client.get(
            f"/sijoituspaikka/{sijoitus.sijoituspaikan_nro}/tarkastusmerkinta",
            params={"page": 1, "page_size": 50},
        ).json()

        assert body["total"] > 0
        for item in body["items"]:
            assert item["sijoituspaikan_nro"] == sijoitus.sijoituspaikan_nro

    def test_nested_route_nonexistent_parent_returns_empty(self, client):
        body = client.get(
            "/hankintatiedot/-99999/alkuperaa_koskevat_tiedot",
            params={"page": 1, "page_size": 10},
        ).json()
        assert body["total"] == 0
        assert body["items"] == []
        assert body["pages"] == 0

    def test_nested_route_respects_page_size(self, client, db_session):
        hankinta = (
            db_session.query(Hankintatiedot)
            .join(AlkuperaaKoskevatTiedot,
                  Hankintatiedot.hankintaID == AlkuperaaKoskevatTiedot.hankintaID)
            .first()
        )
        if not hankinta:
            pytest.skip("No data")

        body = client.get(
            f"/hankintatiedot/{hankinta.hankintaID}/alkuperaa_koskevat_tiedot",
            params={"page": 1, "page_size": 1},
        ).json()
        assert body["page_size"] == 1
        assert len(body["items"]) <= 1

    def test_nested_route_supports_column_filtering(self, client, db_session):
        """Nested routes also run apply_filters so extra query params work."""
        hankinta = (
            db_session.query(Hankintatiedot)
            .join(AlkuperaaKoskevatTiedot,
                  Hankintatiedot.hankintaID == AlkuperaaKoskevatTiedot.hankintaID)
            .first()
        )
        if not hankinta:
            pytest.skip("No data")

        body = client.get(
            f"/hankintatiedot/{hankinta.hankintaID}/alkuperaa_koskevat_tiedot",
            params={"page": 1, "page_size": 10, "alkupera_nro": -99999},
        ).json()
        assert body["total"] == 0

    def test_all_nested_routes_return_200(self, client, db_session):
        """Every /{id}/{child} route must respond without 500."""
        for route in client.app.router.routes:
            if "GET" not in getattr(route, "methods", set()):
                continue
            path = route.path
            # Nested routes: exactly one {param} followed by /child_name
            import re
            if not re.match(r"^/\w+/\{[^}]+\}/\w+$", path):
                continue

            model = _get_module_model(route)
            if model is None:
                continue

            # Resolve the path param with a real DB value
            resolved = path
            for param in route.dependant.path_params:
                col = next(
                    (c for c in model.__table__.columns if c.key == param.name), None
                )
                if col is None:
                    break
                row = db_session.query(model).filter(col.isnot(None)).first()
                if row is None:
                    break
                resolved = resolved.replace(f"{{{param.name}}}", str(getattr(row, col.key)))
            else:
                r = client.get(resolved, params={"page": 1, "page_size": 1})
                assert r.status_code == 200, f"GET {resolved} (from {path}) → {r.status_code}"


# ═══════════════════════════════════════════════════════════════════════════════
# 6. OPENAPI DOCS — filter params are visible
# ═══════════════════════════════════════════════════════════════════════════════

class TestOpenAPIFilterParams:

    def _get_taksoni_params(self, client) -> set[str]:
        schema = client.get("/openapi.json").json()
        return {p["name"] for p in schema["paths"]["/taksoni/"]["get"].get("parameters", [])}

    def test_search_param_is_documented(self, client):
        assert "search" in self._get_taksoni_params(client)

    def test_page_and_page_size_are_documented(self, client):
        params = self._get_taksoni_params(client)
        assert "page" in params
        assert "page_size" in params

    def test_model_pk_column_is_documented_as_filter_param(self, client):
        assert "taksonin_nro" in self._get_taksoni_params(client)

    def test_model_string_column_is_documented_as_filter_param(self, client):
        # 'suku' is a string column on Taksoni
        assert "suku" in self._get_taksoni_params(client)

    def test_alkuperaa_koskevat_tiedot_exposes_hankintaid_filter(self, client):
        schema = client.get("/openapi.json").json()
        params = {
            p["name"] for p in
            schema["paths"]["/alkuperaa_koskevat_tiedot/"]["get"].get("parameters", [])
        }
        assert "hankintaID" in params

    def test_filter_params_have_correct_types_in_schema(self, client):
        schema = client.get("/openapi.json").json()
        params = {
            p["name"]: p
            for p in schema["paths"]["/taksoni/"]["get"].get("parameters", [])
        }
        # page must be integer, not required
        assert params["page"]["schema"]["type"] == "integer"
        assert params["page"].get("required", False) is False
        # search must be string, not required
        assert params["search"]["schema"]["type"] == "string"
        assert params["search"].get("required", False) is False

    def test_all_paginated_list_endpoints_have_search_param(self, client):
        schema = client.get("/openapi.json").json()
        for path, path_item in schema["paths"].items():
            if "get" not in path_item:
                continue
            if "{" in path:
                continue
            param_names = {p["name"] for p in path_item["get"].get("parameters", [])}
            # Only endpoints with make_filter_dep have search documented
            if "page" in param_names and "page_size" in param_names:
                assert "search" in param_names, (
                    f"GET {path} has pagination but no 'search' param in docs"
                )
