# Changelog

All notable changes to the Trace Causality Chain Protocol will be documented in this file.

The project follows an experimental pre-1.0 development model.

## [0.1.0] - 2026-07-07

### Added

* Initial protocol structure.
* `Causality Link Record` JSON Schema.
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

v0.1 introduces:

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

v0.1 establishes the principle that causal attribution must remain distinct from:

* chronological order;
* structural similarity;
* influence;
* independent convergence.

Causal claims should be recorded as evidence-backed and reviewable assessments rather than unquestionable facts.

### Scope

Version 0.1 is intentionally limited to one atomic causal relationship:

```text
Cause Event
     ↓
Effect Event
```

Longer causal chains, delegation lineage, action-to-artifact binding, contribution graphs, and royalty readiness are reserved for later versions.
