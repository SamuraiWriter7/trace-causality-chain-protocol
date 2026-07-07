from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parent.parent

VALIDATION_TARGETS = [
    {
        "name": "Causality Link Record",
        "schema": ROOT / "schemas" / "causality-link-record.schema.json",
        "example": ROOT / "examples" / "causality-link-record.example.yaml",
    }
]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML object at the root.")

    return data


def validate_target(name: str, schema_path: Path, example_path: Path) -> bool:
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )

    errors = sorted(
        validator.iter_errors(example),
        key=lambda error: list(error.absolute_path),
    )

    if errors:
        for error in errors:
            location = ".".join(str(part) for part in error.absolute_path)
            location = location or "<root>"
            print(f"Error: {location}: {error.message}")

        return False

    print(f"[ok] {example_path.name} is valid")
    return True


def main() -> int:
    all_valid = True

    for target in VALIDATION_TARGETS:
        is_valid = validate_target(
            target["name"],
            target["schema"],
            target["example"],
        )
        all_valid = all_valid and is_valid

    if not all_valid:
        print("[failed] validation errors detected")
        return 1

    print("[success] all examples are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
