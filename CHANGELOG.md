# Changelog

All notable changes to the Trace Causality Chain Protocol are documented in this file.

The project follows an experimental pre-1.0 development model.

## [0.5.0] - 2026-07-07

### Added

* Unified Causality Lifecycle schema.
* Unified lifecycle example.
* Root Context model.
* Lifecycle Stage model.
* Lifecycle Record Link model.
* Canonical lifecycle stage sequence.
* Link-level evidence references.
* Link-level confidence assessment.
* Audit Bridge.
* Audit findings summary.
* Blocking condition records.
* Proceed permission state.
* Royalty Readiness model.
* Readiness Check model.
* Human Gate model.
* Conditional approval support.
* Explicit allocation boundary.
* Unified lifecycle documentation.
* Lifecycle semantic validation.
* Required lifecycle-stage validation.
* Stage identifier uniqueness validation.
* Sequence uniqueness validation.
* Link identifier uniqueness validation.
* Stage reference validation.
* Canonical stage-order validation.
* Question-to-Human-Gate reachability validation.
* Audit progression consistency validation.
* Financial allocation boundary validation.

### Lifecycle Stages

v0.5 introduces:

* `question`
* `trace`
* `causality`
* `delegation`
* `action`
* `artifact_binding`
* `contribution_graph`
* `audit`
* `royalty_readiness`
* `human_gate`

### Lifecycle Link Types

v0.5 introduces:

* `initiated`
* `recorded_as`
* `causally_linked`
* `delegated_into`
* `executed_as`
* `bound_into`
* `aggregated_into`
* `audited_by`
* `assessed_for_readiness`
* `submitted_to_gate`
* `other`

### Audit States

v0.5 introduces:

* `not_requested`
* `pending`
* `passed`
* `passed_with_conditions`
* `failed`
* `disputed`

### Royalty Readiness States

v0.5 introduces:

* `not_assessed`
* `not_ready`
* `conditionally_ready`
* `ready`
* `blocked`
* `disputed`

### Readiness Check Types

v0.5 introduces:

* `provenance_complete`
* `contribution_graph_valid`
* `audit_passed`
* `rights_reviewed`
* `disputes_resolved`
* `human_approval_required`
* `custom`

### Human Gate States

v0.5 introduces:

* `not_required`
* `pending`
* `approved`
* `approved_with_conditions`
* `rejected`
* `deferred`
* `disputed`

### Allocation Boundary

v0.5 explicitly establishes that the Unified Causality Lifecycle ends before financial allocation.

The protocol requires:

```text
financial_allocation_executed: false
```

The lifecycle progression is:

```text
Causal Evidence
      ↓
Contribution Graph
      ↓
Audit
      ↓
Royalty Readiness
      ↓
Human Gate

------ Protocol Boundary ------

      ↓
Allocation Policy
      ↓
Settlement
      ↓
Royalty Distribution
```

### Design Principle

v0.5 establishes the Unified Causality Lifecycle as a reference-oriented integration layer.

The lifecycle does not duplicate all underlying records.

Instead, it connects:

* question records;
* trace records;
* causality records;
* delegation records;
* action receipts;
* artifact bindings;
* contribution graphs;
* audit records;
* readiness assessments;
* human-gate decisions.

### Semantic Validation

v0.5 extends validation beyond Schema and Graph validation.

Lifecycle validation checks:

* required stage presence;
* stage identifier uniqueness;
* sequence uniqueness;
* lifecycle-link uniqueness;
* valid Stage references;
* canonical Stage ordering;
* self-loop prevention;
* complete lifecycle reachability;
* Audit Bridge consistency;
* allocation boundary preservation.

### First Arc Completion

v0.5 completes the first protocol arc:

```text
v0.1
Causality Link Record
        ↓
v0.2
Delegation Causality Chain
        ↓
v0.3
Action-to-Artifact Binding
        ↓
v0.4
Contribution Causality Graph
        ↓
v0.5
Unified Causality Lifecycle
```

---

## [0.4.0] - 2026-07-07

### Added

* Contribution Causality Graph schema.
* Contributor registry.
* Contribution nodes.
* Contribution edges.
* Causal role classification.
* Materiality classification.
* Node confidence.
* Edge confidence.
* Graph policy.
* Semantic graph validation.

### Design Principle

v0.4 established that contribution causality and financial allocation must remain separate layers.

---

## [0.3.0] - 2026-07-07

### Added

* Action Artifact Binding schema.
* Action references.
* Artifact references.
* Artifact fragment scope.
* Transformation chains.
* Binding types.
* Binding confidence.
* Verification states.

### Design Principle

v0.3 established that actions should be bindable to specific artifact fragments rather than automatically attributed to entire artifacts.

---

## [0.2.0] - 2026-07-07

### Added

* Delegation Causality Chain schema.
* Root Intent model.
* Participant registry.
* Delegation Steps.
* Authority Scope.
* Constraint Inheritance.
* Redelegation controls.
* Delegation depth limits.

### Design Principle

v0.2 established that delegation is not equivalent to unlimited authority.

---

## [0.1.0] - 2026-07-07

### Added

* Initial protocol structure.
* Causality Link Record schema.
* Evidence Reference model.
* Cause and Effect Event references.
* Relation classification.
* Causality Confidence.
* Human Review state.
* Validation workflow.

### Design Principle

v0.1 established that causality must remain distinct from chronology, similarity, influence, and independent convergence.

