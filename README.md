# Trace Causality Chain Protocol

An open protocol for recording causal links from human questions and origin traces through agent delegation, actions, transformations, artifacts, audits, and royalty readiness.

## Overview

AI-generated outcomes increasingly emerge from distributed chains of human decisions, agent delegation, tool execution, transformation, selection, and review.

A human may create the original question.

An agent may structure it.

A second agent may perform analysis.

A tool may calculate results.

Another agent may transform those results.

A human may select, edit, and approve the final artifact.

The Trace Causality Chain Protocol provides machine-readable records for preserving relationships across this lifecycle.

```text
Question
   ↓
Trace
   ↓
Root Intent
   ↓
Delegation
   ↓
Agent Action
   ↓
Transformation
   ↓
Artifact
   ↓
Audit
   ↓
Contribution Assessment
   ↓
Royalty Readiness
```

The protocol develops this lifecycle incrementally.

---

## Core Principles

### Evidence Before Attribution

Causal and contribution claims should reference visible evidence.

### Similarity Is Not Causation

Temporal precedence, structural similarity, influence, contribution, direct causation, and independent convergence should remain distinguishable.

### Delegation Is Not Unlimited Authority

Delegated work may carry explicit permissions, prohibitions, redelegation rules, and delegation-depth limits.

### Constraints Should Survive Delegation

When tasks move between agents, inherited constraints should remain visible.

### Artifacts Are Composed of Contributions

An action may contribute to an entire artifact or only to a specific fragment.

### Generation Is Not the Only Contribution

Selection, editing, assembly, verification, annotation, and rejection may all be relevant parts of an artifact's causal history.

### Machine Assessment Is Not Final Authority

Machine-generated causal and contribution assessments may require human review.

---

# v0.1 — Causality Link Record

Version 0.1 introduced the atomic causal relationship:

```text
Cause Event
     ↓
Effect Event
```

A Causality Link Record contains:

* cause event;
* effect event;
* relationship type;
* evidence references;
* causality confidence;
* review state.

Supported relationship types include:

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

The central principle is:

> A causal relationship should be expressed as an evidence-backed, reviewable assessment rather than an unquestionable fact.

---

# v0.2 — Delegation Causality Chain

Version 0.2 introduced structured delegation lineage.

```text
Human
  ↓
Agent A
  ↓
Sub-Agent B
  ↓
Tool C
  ↓
Result
```

Each chain begins with a root intent.

Each delegation step may record:

* delegator;
* delegatee;
* delegated task;
* delegation type;
* authority scope;
* inherited constraints;
* redelegation permission;
* maximum delegation depth;
* parent step;
* execution status;
* result references.

## Authority Scope

Delegation may define:

```text
Allowed Actions
Prohibited Actions
Redelegation Allowed
Maximum Delegation Depth
```

Delegation should not be interpreted as unlimited authority.

## Constraint Inheritance

Supported inheritance modes are:

* `strict`
* `bounded_extension`
* `explicit_override`
* `none`

The purpose is to preserve the visibility of constraints as tasks move through multi-agent systems.

---

# v0.3 — Action-to-Artifact Binding

Version 0.3 connects actions and transformation chains to artifacts.

The simplest structure is:

```text
Action
   ↓
Artifact
```

A more realistic structure is:

```text
Delegated Action
       ↓
Intermediate Output
       ↓
Transformation
       ↓
Human Selection
       ↓
Human Edit
       ↓
Final Artifact
```

v0.3 introduces the Action Artifact Binding record.

A binding contains:

* action reference;
* artifact reference;
* binding type;
* contribution scope;
* optional transformation chain;
* evidence references;
* binding confidence;
* verification status.

## Artifact Fragment Binding

An action does not need to be attributed to an entire artifact.

A binding may target:

* whole artifact;
* section;
* file;
* JSON Pointer;
* line range;
* byte range;
* time range;
* custom scope.

Example:

```text
Report
├── Chapter 1 ← Human Research
├── Chapter 2 ← Agent Analysis
├── Table 1   ← Tool Execution
└── Conclusion
      ├── Agent Synthesis
      └── Human Selection and Edit
```

This allows complex collaborative artifacts to retain finer-grained causal lineage.

## Binding Types

v0.3 supports:

* `generated`
* `transformed`
* `assembled`
* `edited`
* `selected`
* `verified`
* `annotated`
* `rejected`
* `other`

These types distinguish production from other meaningful activities.

For example:

```text
Agent A
→ generated candidate outputs

Human B
→ selected one output

Human B
→ edited the selected output

Agent C
→ verified the result
```

These are separate bindings.

## Transformation Chains

An optional transformation chain may record intermediate material transformations.

```text
Trace
  ↓
Analysis
  ↓
Summary
  ↓
Draft
  ↓
Edit
  ↓
Artifact
```

Each transformation step may identify:

* type;
* inputs;
* output;
* actor;
* timestamp.

This creates a bridge between action receipts and final artifact provenance.

## Relationship Between v0.1, v0.2, and v0.3

```text
v0.1
What event relates to what event?
        ↓
v0.2
Who delegated what to whom?
        ↓
v0.3
Which action contributed to which artifact region?
```

Together:

```text
Question
   ↓
Trace
   ↓
Root Intent
   ↓
Delegation Chain
   ↓
Delegation Step
   ↓
Action
   ↓
Action Receipt
   ↓
Transformation Chain
   ↓
Action Artifact Binding
   ↓
Artifact Fragment
```

---

# Repository Structure

```text
schemas/
  causality-link-record.schema.json
  delegation-causality-chain.schema.json
  action-artifact-binding.schema.json

examples/
  causality-link-record.example.yaml
  delegation-causality-chain.example.yaml
  action-artifact-binding.example.yaml

scripts/
  validate_examples.py

docs/
  causality-link-record.md
  delegation-causality-chain.md
  action-to-artifact-binding.md
```

---

# Validation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run validation:

```bash
python scripts/validate_examples.py
```

Expected result:

```text
[validate] Causality Link Record
[ok] causality-link-record.example.yaml is valid

[validate] Delegation Causality Chain
[ok] delegation-causality-chain.example.yaml is valid

[validate] Action Artifact Binding
[ok] action-artifact-binding.example.yaml is valid

[success] all examples are valid
```

---

# Roadmap

## v0.1 — Causality Link Record

Define an atomic evidence-backed relationship between a cause event and an effect event.

## v0.2 — Delegation Causality Chain

Trace root intent, task delegation, authority scope, constraint inheritance, redelegation, and result return.

## v0.3 — Action-to-Artifact Binding

Bind actions and transformations to artifacts or specific artifact fragments.

## v0.4 — Contribution Causality Graph

Represent multiple causal contributions to one or more artifacts without prematurely converting them into financial allocation.

## v0.5 — Unified Causality Lifecycle

Connect questions, traces, delegation, actions, transformations, artifacts, audits, contribution assessment, and royalty readiness.

---

# Design Position

The protocol is designed as a connective causality layer.

```text
Trace Systems
      ↓
Causality Links
      ↓
Delegation Chains
      ↓
Action Receipts
      ↓
Artifact Bindings
      ↓
Contribution Graphs
      ↓
Audit Systems
      ↓
Royalty Readiness
```

The protocol does not attempt to replace these surrounding systems.

Its role is to preserve the causal paths connecting them.

---

# Philosophy

Complex outcomes rarely have one author, one action, or one cause.

An AI-era artifact may emerge from:

* a human question;
* inherited traces;
* agent analysis;
* sub-agent delegation;
* tool execution;
* external sources;
* intermediate transformations;
* human selection;
* human editing;
* machine verification;
* human approval.

The purpose of the protocol is not to flatten this complexity into a single ownership claim.

Its purpose is to preserve the lineage.

Before asking:

> Who owns this?

or:

> How much should each participant receive?

a system should first be able to ask:

> Where did this begin?

> Who inherited the task?

> What authority was transferred?

> What actions occurred?

> What transformations took place?

> Which parts of the artifact are connected to which actions?

> What evidence supports those connections?

Trace Causality Chain Protocol is an attempt to make those questions machine-readable.

## Status

Experimental specification.

Current version: **v0.3**

The protocol is under active structural development.

