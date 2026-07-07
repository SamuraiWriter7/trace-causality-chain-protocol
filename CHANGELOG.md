# Changelog

All notable changes to the Trace Causality Chain Protocol will be documented in this file.

The project follows an experimental pre-1.0 development model.

## [0.4.0] - 2026-07-07

### Added

* Contribution Causality Graph schema.
* Contribution graph example.
* Contributor registry.
* Contribution node model.
* Contribution edge model.
* Artifact reference registry.
* Causal role classification.
* Ordinal materiality classification.
* Node-level confidence assessment.
* Edge-level confidence assessment.
* Graph-level confidence assessment.
* Graph policy configuration.
* Multi-parent contribution support.
* Optional multiple-root support.
* Acyclic graph expectation policy.
* Semantic graph validation.
* Duplicate contributor ID detection.
* Duplicate node ID detection.
* Duplicate edge ID detection.
* Unknown contributor reference detection.
* Unknown artifact reference detection.
* Unknown node reference detection.
* Self-loop detection.
* Cycle detection for acyclic graphs.
* Multiple-root policy validation.
* Multiple-parent policy validation.
* Contribution Causality Graph documentation.

### Contribution Types

v0.4 introduces:

* `origin_question`
* `trace_creation`
* `analysis`
* `generation`
* `transformation`
* `selection`
* `editing`
* `assembly`
* `orchestration`
* `tool_execution`
* `verification`
* `annotation`
* `rejection`
* `context_provision`
* `other`

### Causal Roles

v0.4 introduces:

* `root_origin`
* `enabling`
* `direct`
* `contributing`
* `transformative`
* `selective`
* `corrective`
* `verification`
* `orchestration`
* `contextual`
* `undetermined`

### Materiality Levels

v0.4 introduces:

* `critical`
* `major`
* `moderate`
* `minor`
* `undetermined`

Materiality is intentionally ordinal.

It does not represent:

* royalty percentage;
* ownership percentage;
* legal authorship percentage;
* monetary value.

### Edge Relationship Types

v0.4 introduces:

* `derived_from`
* `enabled`
* `influenced`
* `transformed_into`
* `selected_into`
* `edited_into`
* `assembled_with`
* `verified_by`
* `constrained_by`
* `depends_on`
* `superseded_by`
* `other`

### Design Principle

v0.4 establishes the principle that contribution causality and economic allocation should remain separate layers.

The protocol defines the following progression:

```text
Causal Evidence
      ↓
Contribution Graph
      ↓
Contribution Assessment
      ↓
Allocation Readiness
      ↓
Policy Evaluation
      ↓
Royalty Allocation
```

The Contribution Causality Graph ends before financial allocation.

### Node and Edge Confidence

v0.4 separates confidence in the existence or classification of a contribution event from confidence in the causal relationship connecting events.

```text
Node Confidence
       ≠
Edge Confidence
```

This allows uncertain causal relationships to remain visible.

### Semantic Validation

v0.4 introduces semantic graph validation in addition to JSON Schema validation.

The validator checks graph-level consistency including:

* unique identifiers;
* valid references;
* self-loops;
* root-count policy;
* parent-count policy;
* acyclicity where required.

### Scope

Version 0.4 focuses on:

```text
Contribution Nodes
       ↓
Causal Relationships
       ↓
Branching
       ↓
Convergence
       ↓
Transformation
       ↓
Artifact Formation
```

Financial allocation and royalty execution remain outside the scope of v0.4.

---

## [0.3.0] - 2026-07-07

### Added

* Action Artifact Binding schema.
* Action-to-artifact example record.
* Action reference model.
* Artifact reference model.
* Optional artifact content hash.
* Action Receipt references.
* Delegation Chain references.
* Delegation Step references.
* Artifact fragment contribution scopes.
* Binding type classification.
* Transformation Chain records.
* Evidence-backed binding assessment.
* Binding confidence model.
* Verification status model.
* Human review record.
* Action-to-Artifact Binding documentation.
* Three-schema validation workflow.

### Design Principle

v0.3 established the principle that an action should be bindable to a specific artifact fragment rather than automatically attributed to an entire artifact.

---

## [0.2.0] - 2026-07-07

### Added

* Delegation Causality Chain schema.
* Root intent model.
* Participant registry.
* Delegation step records.
* Authority scope model.
* Constraint inheritance model.
* Parent delegation relationships.
* Handoff references.
* Result references.
* Chain lifecycle status.

### Design Principle

v0.2 established the principle that delegation is not equivalent to unlimited authority.

---

## [0.1.0] - 2026-07-07

### Added

* Initial protocol structure.
* Causality Link Record schema.
* Cause and effect event references.
* Evidence reference model.
* Relationship classification.
* Causality confidence assessment.
* Human review state.
* Validation workflow.
* Initial documentation.

### Design Principle

v0.1 established the principle that causality must remain distinct from chronology, similarity, influence, and independent convergence.
