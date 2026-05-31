from __future__ import annotations

import ast
import importlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENDPOINTS_DIR = ROOT / "app" / "api" / "endpoints"


def _load_module(module_path: Path):
    module_rel = module_path.relative_to(ROOT).with_suffix("")
    module_name = ".".join(module_rel.parts)
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    return importlib.import_module(module_name)


def _find_function(tree: ast.AST, name: str) -> list[ast.FunctionDef]:
    return [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name == name]


def _model_attrs_in_function(func: ast.FunctionDef) -> set[str]:
    attrs: set[str] = set()
    for node in ast.walk(func):
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id == "Model":
            attrs.add(node.attr)
    return attrs


def _update_item_fields(func: ast.FunctionDef) -> set[str]:
    fields: set[str] = set()
    for node in ast.walk(func):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "update_item":
            if len(node.args) >= 4 and isinstance(node.args[3], ast.Constant) and isinstance(node.args[3].value, str):
                fields.add(node.args[3].value)
    return fields


def test_read_one_and_update_one_fields_exist_on_model():
    for path in sorted(ENDPOINTS_DIR.glob("*.py")):
        if path.name in {"__init__.py", ".instructions.md", "auth.py"}:
            continue
        module = _load_module(path)
        model = getattr(module, "Model", None)
        assert model is not None, f"Missing Model import in {path}"

        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source)

        for func in _find_function(tree, "read_one"):
            attrs = _model_attrs_in_function(func)
            assert attrs, f"No Model attributes used in read_one of {path}"
            for attr in attrs:
                assert hasattr(model, attr), f"{path} read_one uses Model.{attr} which does not exist"

        for func in _find_function(tree, "update_one"):
            fields = _update_item_fields(func)
            assert fields, f"No update_item field found in update_one of {path}"
            for field in fields:
                assert hasattr(model, field), f"{path} update_one uses field '{field}' which does not exist on Model"
