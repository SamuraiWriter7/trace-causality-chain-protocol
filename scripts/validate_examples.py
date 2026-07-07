from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parent.parent


VALIDATION_TARGETS = [
    {
        "name": "Causality Link Record",
        "schema": ROOT
        / "schemas"
        / "causality-link-record.schema.json",
        "example": ROOT
        / "examples"
        / "causality-link-record.example.yaml",
    },
    {
        "name": "Delegation Causality Chain",
        "schema": ROOT
        / "schemas"
        / "delegation-causality-chain.schema.json",
        "example": ROOT
        / "examples"
        / "delegation-causality-chain.example.yaml",
    },
    {
        "name": "Action Artifact Binding",
        "schema": ROOT
        / "schemas"
        / "action-artifact-binding.schema.json",
        "example": ROOT
        / "examples"
        / "action-artifact-binding.example.yaml",
    },
    {
        "name": "Contribution Causality Graph",
        "schema": ROOT
        / "schemas"
        / "contribution-causality-graph.schema.json",
        "example": ROOT
        / "examples"
        / "contribution-causality-graph.example.yaml",
        "semantic_validator": "contribution_graph",
    },
]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError(
            f"{path} must contain a YAML object at the root."
        )

    return data


def find_duplicates(values: list[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()

    for value in values:
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)

    return duplicates


def graph_has_cycle(
    node_ids: set[str],
    adjacency: dict[str, list[str]],
) -> bool:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node_id: str) -> bool:
        if node_id in visiting:
            return True

        if node_id in visited:
            return False

        visiting.add(node_id)

        for neighbor in adjacency.get(node_id, []):
            if visit(neighbor):
                return True

        visiting.remove(node_id)
        visited.add(node_id)

        return False

    return any(
        visit(node_id)
        for node_id in node_ids
        if node_id not in visited
    )


def validate_contribution_graph(
    example: dict[str, Any],
) -> list[str]:
    errors: list[str] = []

    contributors = example.get("contributors", [])
    nodes = example.get("contribution_nodes", [])
    edges = example.get("contribution_edges", [])
    artifacts = example.get("artifact_refs", [])
    graph_policy = example.get("graph_policy", {})

    contributor_ids = [
        item["contributor_id"]
        for item in contributors
    ]

    node_ids = [
        item["node_id"]
        for item in nodes
    ]

    edge_ids = [
        item["edge_id"]
        for item in edges
    ]

    artifact_ids = [
        item["artifact_id"]
        for item in artifacts
    ]

    for duplicate in sorted(
        find_duplicates(contributor_ids)
    ):
        errors.append(
            f"duplicate contributor_id: {duplicate}"
        )

    for duplicate in sorted(
        find_duplicates(node_ids)
    ):
        errors.append(
            f"duplicate node_id: {duplicate}"
        )

    for duplicate in sorted(
        find_duplicates(edge_ids)
    ):
        errors.append(
            f"duplicate edge_id: {duplicate}"
        )

    contributor_id_set = set(contributor_ids)
    node_id_set = set(node_ids)
    artifact_id_set = set(artifact_ids)

    for node in nodes:
        node_id = node["node_id"]
        contributor_id = node["contributor_id"]

        if contributor_id not in contributor_id_set:
            errors.append(
                f"{node_id}: unknown contributor_id "
                f"{contributor_id}"
            )

        scope = node.get("contribution_scope", {})
        artifact_id = scope.get("artifact_id")

        if (
            artifact_id is not None
            and artifact_id not in artifact_id_set
        ):
            errors.append(
                f"{node_id}: unknown artifact_id "
                f"{artifact_id}"
            )

    adjacency: dict[str, list[str]] = defaultdict(list)
    incoming_count: dict[str, int] = defaultdict(int)

    for edge in edges:
        edge_id = edge["edge_id"]
        from_node = edge["from_node_id"]
        to_node = edge["to_node_id"]

        if from_node not in node_id_set:
            errors.append(
                f"{edge_id}: unknown from_node_id "
                f"{from_node}"
            )

        if to_node not in node_id_set:
            errors.append(
                f"{edge_id}: unknown to_node_id "
                f"{to_node}"
            )

        if from_node == to_node:
            errors.append(
                f"{edge_id}: self-loop is not allowed"
            )

        if (
            from_node in node_id_set
            and to_node in node_id_set
        ):
            adjacency[from_node].append(to_node)
            incoming_count[to_node] += 1

    if graph_policy.get("acyclic_expected", False):
        if graph_has_cycle(node_id_set, adjacency):
            errors.append(
                "graph contains a cycle while "
                "acyclic_expected is true"
            )

    root_nodes = [
        node_id
        for node_id in node_ids
        if incoming_count[node_id] == 0
    ]

    if (
        not graph_policy.get(
            "multiple_roots_allowed",
            True,
        )
        and len(root_nodes) > 1
    ):
        errors.append(
            "multiple root nodes detected while "
            "multiple_roots_allowed is false: "
            + ", ".join(sorted(root_nodes))
        )

    if not graph_policy.get(
        "multiple_parents_allowed",
        True,
    ):
        for node_id, count in incoming_count.items():
            if count > 1:
                errors.append(
                    f"{node_id}: multiple parents detected "
                    "while multiple_parents_allowed is false"
                )

    return errors


def validate_target(
    name: str,
    schema_path: Path,
    example_path: Path,
    semantic_validator: str | None = None,
) -> bool:
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )

    schema_errors = sorted(
        validator.iter_errors(example),
        key=lambda error: list(error.absolute_path),
    )

    if schema_errors:
        for error in schema_errors:
            location = ".".join(
                str(part)
                for part in error.absolute_path
            )
            location = location or "<root>"

            print(
                f"Error: {location}: {error.message}"
            )

        return False

    semantic_errors: list[str] = []

    if semantic_validator == "contribution_graph":
        semantic_errors = validate_contribution_graph(
            example
        )

    if semantic_errors:
        for error in semantic_errors:
            print(f"Error: semantic: {error}")

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
            target.get("semantic_validator"),
        )

        all_valid = all_valid and is_valid

    if not all_valid:
        print("[failed] validation errors detected")
        return 1

    print("[success] all examples are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
