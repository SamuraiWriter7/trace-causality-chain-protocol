# Changelog

All notable changes to the Trace Causality Chain Protocol will be documented in this file.

The project follows an experimental pre-1.0 development model.

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

### Binding Types

v0.3 introduces:

* `generated`
* `transformed`
* `assembled`
* `edited`
* `selected`
* `verified`
* `annotated`
* `rejected`
* `other`

### Contribution Scope Types

v0.3 introduces:

* `whole_artifact`
* `section`
* `file`
* `json_pointer`
* `line_range`
* `byte_range`
* `time_range`
* `custom`

### Transformation Types

v0.3 introduces:

* `summarization`
* `translation`
* `rewriting`
* `code_generation`
* `code_modification`
* `aggregation`
* `filtering`
* `conversion`
* `human_edit`
* `model_edit`
* `other`

### Design Principle

v0.3 establishes the principle that an action should be bindable to a specific artifact fragment rather than being automatically attributed to an entire artifact.

The protocol distinguishes:

```text
Artifact Identity
        ≠
Contribution Scope
```

An artifact may contain contributions from multiple humans, agents, tools, and transformation processes.

### Selection as Contribution

v0.3 recognizes selection as distinct from generation.

For example:

```text
Agent
→ generates candidates

Human
→ selects candidate

Human
→ edits candidate

Verifier
→ verifies result
```

These activities may be recorded as separate bindings.

v0.3 does not assign financial values to these activities.

### Verification Without Authorship

Verification may be recorded independently from generation or editing.

A participant that verifies an artifact is not automatically represented as its generator or author.

### Scope

Version 0.3 focuses on:

```text
Delegated Action
       ↓
Action Receipt
       ↓
Transformation
       ↓
Artifact Binding
       ↓
Artifact Fragment
```

Contribution graph construction and royalty allocation remain outside the scope of v0.3.

---

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

v0.2 introduced:

* `human_to_agent`
* `agent_to_agent`
* `agent_to_sub_agent`
* `agent_to_tool`
* `system_to_agent`
* `handoff`
* `result_return`
* `other`

### Constraint Inheritance Modes

v0.2 introduced:

* `strict`
* `bounded_extension`
* `explicit_override`
* `none`

### Design Principle

v0.2 established the principle that delegation is not equivalent to unlimited authority.

Delegated work should preserve the visibility of:

* originating intent;
* task scope;
* allowed actions;
* prohibited actions;
* redelegation rules;
* delegation depth;
* inherited constraints;
* downstream constraint changes.

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

Causal claims should be represented as evidence-backed and reviewable assessments rather than unquestionable facts.
