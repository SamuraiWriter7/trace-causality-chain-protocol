from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parent.parent


REQUIRED_LIFECYCLE_STAGE_TYPES = {
    "question",
    "trace",
    "causality",
    "delegation",
    "action",
    "artifact_binding",
    "contribution_graph",
    "audit",
    "royalty_readiness",
    "human_gate",
}


CANONICAL_STAGE_ORDER = {
    "question": 1,
    "trace": 2,
    "causality": 3,
    "delegation": 4,
    "action": 5,
    "artifact_binding": 6,
    "contribution_graph": 7,
    "audit": 8,
    "royalty_readiness": 9,
    "human_gate": 10,
}


VALIDATION_TARGETS = [
    {
        "name": "Causality Link Record",
        "schema": (
            ROOT
            / "schemas"
            / "causality-link-record.schema.json"
        ),
        "example": (
            ROOT
            / "examples"
            / "causality-link-record.example.yaml"
        ),
    },
    {
        "name": "Delegation Causality Chain",
        "schema": (
            ROOT
            / "schemas"
            / "delegation-causality-chain.schema.json"
        ),
        "example": (
            ROOT
            / "examples"
            / "delegation-causality-chain.example.yaml"
        ),
    },
    {
        "name": "Action Artifact Binding",
        "schema": (
            ROOT
            / "schemas"
            / "action-artifact-binding.schema.json"
        ),
        "example": (
            ROOT
            / "examples"
            / "action-artifact-binding.example.yaml"
        ),
    },
    {
        "name": "Contribution Causality Graph",
        "schema": (
            ROOT
            / "schemas"
            / "contribution-causality-graph.schema.json"
        ),
        "example": (
            ROOT
            / "examples"
            / "contribution-causality-graph.example.yaml"
        ),
        "semantic_validator": "contribution_graph",
    },
    {
        "name": "Unified Causality Lifecycle",
        "schema": (
            ROOT
            / "schemas"
            / "unified-causality-lifecycle.schema.json"
        ),
        "example": (
            ROOT
            / "examples"
            / "unified-causality-lifecycle.example.yaml"
        ),
        "semantic_validator": "unified_lifecycle",
    },
]


def load_json(path: Path) -> dict[str, Any]:
    """
    Load a JSON document and ensure the root is an object.
    """

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError(
            f"{path} must contain a JSON object at the root."
        )

    return data


def load_yaml(path: Path) -> dict[str, Any]:
    """
    Load a YAML document and ensure the root is a mapping.
    """

    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError(
            f"{path} must contain a YAML object at the root."
        )

    return data


def find_duplicates(values: list[Any]) -> set[Any]:
    """
    Return duplicate values from a list.
    """

    seen: set[Any] = set()
    duplicates: set[Any] = set()

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
    """
    Detect whether a directed graph contains a cycle.
    """

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

    for node_id in node_ids:
        if node_id not in visited:
            if visit(node_id):
                return True

    return False


def reachable(
    adjacency: dict[str, list[str]],
    start_nodes: set[str],
    target_nodes: set[str],
) -> bool:
    """
    Return True when at least one target node is reachable
    from at least one start node.
    """

    stack = list(start_nodes)
    visited: set[str] = set()

    while stack:
        node_id = stack.pop()

        if node_id in target_nodes:
            return True

        if node_id in visited:
            continue

        visited.add(node_id)

        for neighbor in adjacency.get(node_id, []):
            if neighbor not in visited:
                stack.append(neighbor)

    return False


def validate_contribution_graph(
    example: dict[str, Any],
) -> list[str]:
    """
    Perform semantic validation for a Contribution
    Causality Graph.

    Checks include:
    - duplicate identifiers
    - invalid contributor references
    - invalid artifact references
    - invalid node references
    - self-loops
    - cycles when acyclic behavior is expected
    - root-count policy
    - parent-count policy
    """

    errors: list[str] = []

    contributors = example.get("contributors", [])
    nodes = example.get("contribution_nodes", [])
    edges = example.get("contribution_edges", [])
    artifacts = example.get("artifact_refs", [])
    graph_policy = example.get("graph_policy", {})

    contributor_ids = [
        contributor["contributor_id"]
        for contributor in contributors
    ]

    node_ids = [
        node["node_id"]
        for node in nodes
    ]

    edge_ids = [
        edge["edge_id"]
        for edge in edges
    ]

    artifact_ids = [
        artifact["artifact_id"]
        for artifact in artifacts
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

    for duplicate in sorted(
        find_duplicates(artifact_ids)
    ):
        errors.append(
            f"duplicate artifact_id: {duplicate}"
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

        contribution_scope = node.get(
            "contribution_scope",
            {},
        )

        artifact_id = contribution_scope.get(
            "artifact_id"
        )

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

    for node_id in node_id_set:
        incoming_count[node_id] = 0

    for edge in edges:
        edge_id = edge["edge_id"]
        from_node_id = edge["from_node_id"]
        to_node_id = edge["to_node_id"]

        if from_node_id not in node_id_set:
            errors.append(
                f"{edge_id}: unknown from_node_id "
                f"{from_node_id}"
            )

        if to_node_id not in node_id_set:
            errors.append(
                f"{edge_id}: unknown to_node_id "
                f"{to_node_id}"
            )

        if from_node_id == to_node_id:
            errors.append(
                f"{edge_id}: self-loop is not allowed"
            )

        if (
            from_node_id in node_id_set
            and to_node_id in node_id_set
            and from_node_id != to_node_id
        ):
            adjacency[from_node_id].append(
                to_node_id
            )

            incoming_count[to_node_id] += 1

    if graph_policy.get("acyclic_expected", False):
        if graph_has_cycle(
            node_id_set,
            adjacency,
        ):
            errors.append(
                "graph contains a cycle while "
                "acyclic_expected is true"
            )

    root_nodes = [
        node_id
        for node_id in node_ids
        if incoming_count[node_id] == 0
    ]

    multiple_roots_allowed = graph_policy.get(
        "multiple_roots_allowed",
        True,
    )

    if (
        not multiple_roots_allowed
        and len(root_nodes) > 1
    ):
        errors.append(
            "multiple root nodes detected while "
            "multiple_roots_allowed is false: "
            + ", ".join(sorted(root_nodes))
        )

    if not root_nodes and node_ids:
        errors.append(
            "no root node detected in contribution graph"
        )

    multiple_parents_allowed = graph_policy.get(
        "multiple_parents_allowed",
        True,
    )

    if not multiple_parents_allowed:
        for node_id, parent_count in (
            incoming_count.items()
        ):
            if parent_count > 1:
                errors.append(
                    f"{node_id}: multiple parents detected "
                    "while multiple_parents_allowed is false"
                )

    return errors


def validate_unified_lifecycle(
    example: dict[str, Any],
) -> list[str]:
    """
    Perform semantic validation for a Unified Causality
    Lifecycle.

    Checks include:
    - duplicate stage IDs
    - duplicate sequence numbers
    - duplicate link IDs
    - required lifecycle stages
    - canonical stage ordering
    - invalid stage references
    - self-loops
    - lifecycle graph cycles
    - question-to-human-gate reachability
    - audit bridge consistency
    - royalty readiness consistency
    - human gate consistency
    - financial allocation boundary preservation
    """

    errors: list[str] = []

    stages = example.get(
        "lifecycle_stages",
        [],
    )

    links = example.get(
        "record_links",
        [],
    )

    stage_ids = [
        stage["stage_id"]
        for stage in stages
    ]

    sequences = [
        stage["sequence"]
        for stage in stages
    ]

    link_ids = [
        link["link_id"]
        for link in links
    ]

    for duplicate in sorted(
        find_duplicates(stage_ids)
    ):
        errors.append(
            f"duplicate stage_id: {duplicate}"
        )

    for duplicate in sorted(
        find_duplicates(sequences)
    ):
        errors.append(
            f"duplicate stage sequence: {duplicate}"
        )

    for duplicate in sorted(
        find_duplicates(link_ids)
    ):
        errors.append(
            f"duplicate lifecycle link_id: {duplicate}"
        )

    stage_id_set = set(stage_ids)

    stage_types_present = {
        stage["stage_type"]
        for stage in stages
    }

    missing_stage_types = (
        REQUIRED_LIFECYCLE_STAGE_TYPES
        - stage_types_present
    )

    for stage_type in sorted(
        missing_stage_types
    ):
        errors.append(
            "required lifecycle stage missing: "
            f"{stage_type}"
        )

    sorted_stages = sorted(
        stages,
        key=lambda stage: stage["sequence"],
    )

    previous_order = 0

    for stage in sorted_stages:
        stage_id = stage["stage_id"]
        stage_type = stage["stage_type"]

        canonical_order = CANONICAL_STAGE_ORDER.get(
            stage_type
        )

        if canonical_order is None:
            errors.append(
                f"{stage_id}: unknown stage_type "
                f"{stage_type}"
            )
            continue

        if canonical_order < previous_order:
            errors.append(
                f"{stage_id}: stage_type "
                f"{stage_type} violates canonical order"
            )

        previous_order = max(
            previous_order,
            canonical_order,
        )

    adjacency: dict[str, list[str]] = defaultdict(list)

    incoming_count: dict[str, int] = defaultdict(int)

    for stage_id in stage_id_set:
        incoming_count[stage_id] = 0

    for link in links:
        link_id = link["link_id"]
        from_stage_id = link["from_stage_id"]
        to_stage_id = link["to_stage_id"]

        if from_stage_id not in stage_id_set:
            errors.append(
                f"{link_id}: unknown from_stage_id "
                f"{from_stage_id}"
            )

        if to_stage_id not in stage_id_set:
            errors.append(
                f"{link_id}: unknown to_stage_id "
                f"{to_stage_id}"
            )

        if from_stage_id == to_stage_id:
            errors.append(
                f"{link_id}: self-loop is not allowed"
            )

        if (
            from_stage_id in stage_id_set
            and to_stage_id in stage_id_set
            and from_stage_id != to_stage_id
        ):
            adjacency[from_stage_id].append(
                to_stage_id
            )

            incoming_count[to_stage_id] += 1

    if graph_has_cycle(
        stage_id_set,
        adjacency,
    ):
        errors.append(
            "lifecycle graph contains a cycle"
        )

    question_stage_ids = {
        stage["stage_id"]
        for stage in stages
        if stage["stage_type"] == "question"
    }

    human_gate_stage_ids = {
        stage["stage_id"]
        for stage in stages
        if stage["stage_type"] == "human_gate"
    }

    if (
        question_stage_ids
        and human_gate_stage_ids
        and not reachable(
            adjacency,
            question_stage_ids,
            human_gate_stage_ids,
        )
    ):
        errors.append(
            "no complete lifecycle path exists from "
            "question stage to human_gate stage"
        )

    audit_bridge = example.get(
        "audit_bridge",
        {},
    )

    audit_status = audit_bridge.get(
        "audit_status"
    )

    proceed_allowed = audit_bridge.get(
        "proceed_allowed"
    )

    blocking_conditions = audit_bridge.get(
        "blocking_conditions",
        [],
    )

    if (
        audit_status == "failed"
        and proceed_allowed is True
    ):
        errors.append(
            "audit_status is failed but "
            "proceed_allowed is true"
        )

    if (
        audit_status == "disputed"
        and proceed_allowed is True
    ):
        errors.append(
            "audit_status is disputed but "
            "proceed_allowed is true"
        )

    if (
        blocking_conditions
        and proceed_allowed is True
    ):
        errors.append(
            "blocking_conditions are present but "
            "proceed_allowed is true"
        )

    royalty_readiness = example.get(
        "royalty_readiness",
        {},
    )

    readiness_status = royalty_readiness.get(
        "readiness_status"
    )

    readiness_checks = royalty_readiness.get(
        "readiness_checks",
        [],
    )

    financial_allocation_executed = (
        royalty_readiness.get(
            "financial_allocation_executed"
        )
    )

    if financial_allocation_executed is not False:
        errors.append(
            "financial allocation must remain outside "
            "the Unified Causality Lifecycle"
        )

    failed_readiness_checks = [
        check["check_id"]
        for check in readiness_checks
        if check.get("result") == "fail"
    ]

    if (
        failed_readiness_checks
        and readiness_status == "ready"
    ):
        errors.append(
            "readiness_status is ready while failed "
            "readiness checks exist: "
            + ", ".join(
                sorted(failed_readiness_checks)
            )
        )

    pending_readiness_checks = [
        check["check_id"]
        for check in readiness_checks
        if check.get("result") == "pending"
    ]

    if (
        pending_readiness_checks
        and readiness_status == "ready"
    ):
        errors.append(
            "readiness_status is ready while pending "
            "readiness checks exist: "
            + ", ".join(
                sorted(pending_readiness_checks)
            )
        )

    human_gate = example.get(
        "human_gate",
        {},
    )

    gate_status = human_gate.get(
        "gate_status"
    )

    gate_conditions = human_gate.get(
        "conditions",
        [],
    )

    if (
        gate_status == "approved"
        and gate_conditions
    ):
        errors.append(
            "human gate is approved but conditions "
            "are still present; use "
            "approved_with_conditions instead"
        )

    if (
        gate_status == "approved_with_conditions"
        and not gate_conditions
    ):
        errors.append(
            "human gate is approved_with_conditions "
            "but no conditions are recorded"
        )

    lifecycle_status = example.get(
        "lifecycle_status"
    )

    if (
        gate_status == "rejected"
        and lifecycle_status
        not in {"blocked", "cancelled", "disputed"}
    ):
        errors.append(
            "human gate is rejected but lifecycle_status "
            f"is {lifecycle_status}"
        )

    if (
        readiness_status == "blocked"
        and lifecycle_status == "completed"
    ):
        errors.append(
            "royalty readiness is blocked but lifecycle_status "
            "is completed"
        )

    return errors


def run_semantic_validation(
    validator_name: str | None,
    example: dict[str, Any],
) -> list[str]:
    """
    Dispatch semantic validation by validator name.
    """

    if validator_name is None:
        return []

    if validator_name == "contribution_graph":
        return validate_contribution_graph(
            example
        )

    if validator_name == "unified_lifecycle":
        return validate_unified_lifecycle(
            example
        )

    return [
        f"unknown semantic validator: {validator_name}"
    ]


def validate_target(
    name: str,
    schema_path: Path,
    example_path: Path,
    semantic_validator: str | None = None,
) -> bool:
    """
    Validate one example against its JSON Schema and,
    when configured, additional semantic rules.
    """

    print(f"[validate] {name}")
    print(
        f"  schema : "
        f"{schema_path.relative_to(ROOT)}"
    )
    print(
        f"  example: "
        f"{example_path.relative_to(ROOT)}"
    )

    try:
        schema = load_json(schema_path)
    except (
        OSError,
        json.JSONDecodeError,
        ValueError,
    ) as error:
        print(
            f"Error: failed to load schema: {error}"
        )
        return False

    try:
        example = load_yaml(example_path)
    except (
        OSError,
        yaml.YAMLError,
        ValueError,
    ) as error:
        print(
            f"Error: failed to load example: {error}"
        )
        return False

    try:
        Draft202012Validator.check_schema(
            schema
        )
    except Exception as error:
        print(
            f"Error: invalid JSON Schema: {error}"
        )
        return False

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )

    schema_errors = sorted(
        validator.iter_errors(example),
        key=lambda error: [
            str(part)
            for part in error.absolute_path
        ],
    )

    if schema_errors:
        for error in schema_errors:
            location = ".".join(
                str(part)
                for part in error.absolute_path
            )

            location = location or "<root>"

            print(
                f"Error: {location}: "
                f"{error.message}"
            )

        return False

    semantic_errors = run_semantic_validation(
        semantic_validator,
        example,
    )

    if semantic_errors:
        for error in semantic_errors:
            print(
                f"Error: semantic: {error}"
            )

        return False

    print(
        f"[ok] {example_path.name} is valid"
    )

    return True


def main() -> int:
    """
    Validate all protocol examples.

    Returns:
        0 when all validation targets pass.
        1 when one or more targets fail.
    """

    all_valid = True

    for target in VALIDATION_TARGETS:
        is_valid = validate_target(
            name=target["name"],
            schema_path=target["schema"],
            example_path=target["example"],
            semantic_validator=target.get(
                "semantic_validator"
            ),
        )

        all_valid = (
            all_valid
            and is_valid
        )

        print()

    if not all_valid:
        print(
            "[failed] validation errors detected"
        )
        return 1

    print(
        "[success] all examples are valid"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
