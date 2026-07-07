# Changelog

All notable changes to the Trace Causality Chain Protocol will be documented in this file.

The project follows an experimental pre-1.0 development model.

## [0.2.0] - 2026-07-07

### Added

* Delegation Causality Chain schema.
* Delegation chain example.
* Root intent model.
* Participant registry.
* Delegation step records.
* Delegator and delegatee relationships.
* Delegation type classification.
* Delegated task model.
* Authority scope model.
* Allowed action declarations.
* Prohibited action declarations.
* Redelegation permission field.
* Maximum delegation depth field.
* Constraint inheritance model.
* Parent delegation step references.
* Optional handoff record references.
* Optional action receipt references.
* Optional result references.
* Chain lifecycle status.
* Causality Link Record references.
* Delegation Causality Chain documentation.
* Multi-schema example validation.

### Delegation Types

v0.2 introduces:

* `human_to_agent`
* `agent_to_agent`
* `agent_to_sub_agent`
* `agent_to_tool`
* `system_to_agent`
* `handoff`
* `result_return`
* `other`

### Constraint Inheritance Modes

v0.2 introduces:

* `strict`
* `bounded_extension`
* `explicit_override`
* `none`

### Design Principle

v0.2 establishes the principle that delegation is not equivalent to unlimited authority.

Delegated work should be able to preserve:

* originating intent;
* task scope;
* allowed actions;
* prohibited actions;
* redelegation rules;
* delegation depth;
* inherited constraints;
* downstream constraint changes.

### Scope

Version 0.2 focuses on delegation lineage:

```text
Root Intent
     ↓
Delegation Step
     ↓
Sub-Delegation
     ↓
Tool Invocation
     ↓
Result Return
```

Action-to-artifact binding, contribution causality graphs, and royalty readiness remain outside the scope of v0.2.

---

## [0.1.0] - 2026-07-07

### Added

* Initial protocol structure.
* Causality Link Record JSON Schema.
* Example YAML record.
* Evidence reference model.
* Cause event and effect event references.
* Explicit causal relationship classification.
* Causality confidence scoring with textual basis.
* Human review status model.
* Optional structured human review record.
* Example validation script.
* GitHub Actions validation workflow.
* Initial protocol documentation.

### Relation Types

v0.1 introduced:

* `direct_cause`
* `contributing_cause`
* `enabling_condition`
* `transformation`
* `delegation`
* `influence`
* `temporal_precedence`
* `structural_similarity`
* `independent_convergence`
* `unknown`

### Design Principle

v0.1 established the principle that causal attribution must remain distinct from:

* chronological order;
* structural similarity;
* influence;
* independent convergence.

Causal claims should be recorded as evidence-backed and reviewable assessments rather than unquestionable facts.

### Scope

Version 0.1 introduced the atomic causal relationship:

```text
Cause Event
     ↓
Effect Event
```

Longer causal chains, delegation lineage, action-to-artifact binding, contribution graphs, and royalty readiness were reserved for later versions.
