# Unified Causality Lifecycle

## Purpose

The Unified Causality Lifecycle connects the protocol layers introduced in v0.1 through v0.4 into one lifecycle-level record.

The lifecycle covers:

```text
Question
   ↓
Trace
   ↓
Causality
   ↓
Delegation
   ↓
Action
   ↓
Artifact Binding
   ↓
Contribution Graph
   ↓
Audit
   ↓
Royalty Readiness
   ↓
Human Gate
```

The purpose of v0.5 is not to replace the underlying records.

Its purpose is to make their lifecycle relationships visible and machine-readable.

## Reference-Oriented Integration

The Unified Causality Lifecycle uses references to external or protocol-local records.

It does not require all underlying records to be duplicated inside one large document.

For example:

```text
Lifecycle Record
├── Question Reference
├── Trace Reference
├── Causality Link Reference
├── Delegation Chain Reference
├── Action Receipt Reference
├── Artifact Binding Reference
├── Contribution Graph Reference
├── Audit Record Reference
├── Royalty Readiness Reference
└── Human Gate Reference
```

This approach keeps each protocol layer independently usable while allowing lifecycle-level integration.

## Lifecycle Stages

A lifecycle contains ordered stages.

Supported stage types are:

* question;
* trace;
* causality;
* delegation;
* action;
* artifact binding;
* contribution graph;
* audit;
* royalty readiness;
* human gate.

A stage records:

* stage identity;
* sequence;
* stage type;
* lifecycle status;
* record references;
* optional actor references;
* optional timestamps.

Multiple stages of the same type may exist.

For example, a lifecycle may contain multiple action stages or multiple audit stages.

## Record Links

Lifecycle stages are connected through Record Links.

A Record Link expresses how one lifecycle stage relates to another.

Supported relationships include:

* initiated;
* recorded as;
* causally linked;
* delegated into;
* executed as;
* bound into;
* aggregated into;
* audited by;
* assessed for readiness;
* submitted to gate;
* other.

Each link contains:

* source stage;
* destination stage;
* relationship type;
* evidence references;
* link confidence.

The existence of two lifecycle stages does not automatically establish a causal relationship between them.

This is why stages and links are separate.

## Lifecycle Order

The canonical lifecycle order is:

```text
Question
   ↓
Trace
   ↓
Causality
   ↓
Delegation
   ↓
Action
   ↓
Artifact Binding
   ↓
Contribution Graph
   ↓
Audit
   ↓
Royalty Readiness
   ↓
Human Gate
```

A lifecycle implementation may contain multiple records within these categories.

However, the lifecycle should preserve the causal direction of the process.

## Audit Bridge

The Audit Bridge connects the Contribution Causality Graph with downstream readiness assessment.

The bridge records:

* audit status;
* audit record references;
* findings;
* blocking conditions;
* whether downstream processing may continue.

Supported audit states include:

* not requested;
* pending;
* passed;
* passed with conditions;
* failed;
* disputed.

The audit bridge is intentionally more expressive than a binary PASS or FAIL result.

Real-world contribution systems may be sufficiently documented for downstream evaluation while still requiring additional rights review or dispute resolution.

## Royalty Readiness

Royalty Readiness asks whether the causal and contribution records are sufficiently mature for downstream allocation policy evaluation.

It does not calculate or execute royalties.

Possible readiness states include:

* not assessed;
* not ready;
* conditionally ready;
* ready;
* blocked;
* disputed.

Readiness checks may include:

* provenance completeness;
* contribution graph validity;
* audit completion;
* rights review;
* dispute resolution;
* human approval requirements.

## Allocation Boundary

The Unified Causality Lifecycle stops before financial allocation.

This boundary is explicit.

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
Contract Evaluation
      ↓
Settlement
      ↓
Royalty Distribution
```

The field:

```text
financial_allocation_executed: false
```

preserves this boundary.

The lifecycle may establish that a case is ready for downstream allocation evaluation.

It does not perform allocation.

## Human Gate

The final lifecycle layer is the Human Gate.

Possible states include:

* not required;
* pending;
* approved;
* approved with conditions;
* rejected;
* deferred;
* disputed.

The gate may record:

* reviewer references;
* decision time;
* conditions;
* decision basis.

The Human Gate exists because lifecycle completeness does not automatically imply legal, ethical, contractual, or economic permission to proceed.

## Conditional Completion

A lifecycle may be:

```text
completed_with_conditions
```

This is important for realistic workflows.

For example:

```text
Provenance: complete
Contribution Graph: valid
Audit: passed
Rights Review: pending
Human Gate: approved with conditions
```

The lifecycle is not failed.

It is also not unconditionally complete.

The protocol preserves this intermediate state.

## Relationship to Earlier Versions

### v0.1 — Causality Link Record

Answers:

> What relationship exists between two events?

### v0.2 — Delegation Causality Chain

Answers:

> Who delegated what to whom, under what authority and constraints?

### v0.3 — Action-to-Artifact Binding

Answers:

> Which action contributed to which artifact or artifact fragment?

### v0.4 — Contribution Causality Graph

Answers:

> How did multiple contributions branch, transform, and converge?

### v0.5 — Unified Causality Lifecycle

Answers:

> How does the entire causal process connect from originating question to audit and royalty readiness?

## Validation Layers

v0.5 supports three conceptual levels of validation.

### Schema Validation

Checks field structure and data types.

### Graph Validation

Checks Contribution Causality Graph consistency.

### Lifecycle Validation

Checks:

* unique stage identifiers;
* unique sequences;
* valid stage references;
* required lifecycle stage presence;
* canonical ordering;
* valid lifecycle links;
* complete reachability from question to human gate;
* audit progression consistency;
* allocation boundary preservation.

## Complete Lifecycle Path

The lifecycle should preserve at least one complete traceable path from the originating question to the final human gate.

Conceptually:

```text
Question
   ↓
Trace
   ↓
Causality
   ↓
Delegation
   ↓
Action
   ↓
Artifact
   ↓
Contribution Graph
   ↓
Audit
   ↓
Readiness
   ↓
Human Gate
```

Branches and multiple actions may exist.

However, the lifecycle should not become a disconnected collection of records.

## Non-Goals of v0.5

Version 0.5 does not attempt to:

* calculate monetary value;
* execute royalty payments;
* determine legal ownership;
* determine copyright authorship;
* replace payment protocols;
* replace settlement systems;
* replace contractual policy engines;
* replace identity systems;
* automatically resolve disputes.

Its purpose is:

> Preserve and connect the causal lifecycle required before downstream value allocation can be responsibly evaluated.

## Civilizational Position

AI systems increasingly produce outputs through distributed causal chains.

The final artifact may be visible.

The chain that produced it may not be.

The Unified Causality Lifecycle treats that hidden chain as infrastructure.

Before an AI economy can distribute value, it needs to preserve causality.

Before causality can support value, it needs evidence.

Before evidence can become allocation, it needs audit, policy, and human review.

The Unified Causality Lifecycle exists to preserve that sequence.
