# Trace Causality Chain Protocol

An open protocol for recording causal links from human questions and origin traces through agent delegation, actions, transformations, artifacts, audits, and royalty readiness.

## Overview

AI systems increasingly operate through chains of interactions rather than isolated prompts and responses.

A human question may create a trace.

That trace may become the root intent for an AI agent.

The agent may delegate analysis to another agent.

A sub-agent may invoke a tool.

The resulting work may be transformed into an artifact, audited, reused, and eventually connected to contribution assessment or value return.

Most existing logs record individual events.

The Trace Causality Chain Protocol focuses on the relationships between them.

The protocol is designed to express:

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

## Core Principles

### Evidence Before Attribution

Causal relationships should be supported by visible evidence references.

### Similarity Is Not Causation

The protocol distinguishes temporal order, structural similarity, influence, contribution, direct causation, and independent convergence.

### Delegation Is Not Unlimited Authority

A delegated task should be able to carry explicit permissions, prohibitions, redelegation rules, and depth limits.

### Constraints Should Survive Delegation

When work moves from one agent to another, inherited constraints should remain visible.

### Machine Assessment Is Not Final Authority

Machine-generated causal assessments and delegation reconstructions may still require human review.

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

Supported relation types include:

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

The purpose of v0.1 is to make causal claims inspectable and reviewable without turning chronological order or similarity into automatic proof of causation.

---

# v0.2 — Delegation Causality Chain

Version 0.2 introduces structured delegation lineage.

A chain may represent:

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

The root intent may reference:

* the originating human;
* a human question;
* an origin trace;
* a summary of the intended objective.

Each delegation step records:

* delegator;
* delegatee;
* delegated task;
* delegation type;
* authority scope;
* constraint inheritance;
* parent step;
* execution status;
* result reference.

## Authority Scope

A delegation step may define:

```text
Allowed Actions
Prohibited Actions
Redelegation Allowed
Maximum Delegation Depth
```

This prevents delegation from being interpreted as unlimited permission.

## Constraint Inheritance

v0.2 defines four constraint inheritance modes:

### `strict`

Inherited constraints remain unchanged.

### `bounded_extension`

Inherited constraints remain active and new downstream constraints may be added.

### `explicit_override`

Inherited constraints may be changed, but the change should be visible and justified.

### `none`

No constraint inheritance is claimed.

## Delegation Types

Supported delegation types include:

* `human_to_agent`
* `agent_to_agent`
* `agent_to_sub_agent`
* `agent_to_tool`
* `system_to_agent`
* `handoff`
* `result_return`
* `other`

## Branching Delegation

Delegation chains may branch.

```text
Human
  ↓
Agent A
  ├──→ Analyst Agent
  ├──→ Verification Agent
  └──→ Tool
```

The `parent_step_id` field allows downstream systems to reconstruct delegation lineage.

---

# Relationship Between v0.1 and v0.2

v0.1 records event relationships.

v0.2 records responsibility and authority propagation.

```text
Causality Link
      ↓
Delegation Step
      ↓
Delegation Chain
```

These layers are related but intentionally separate.

A delegation event does not automatically prove that the final artifact was exclusively caused by the original delegator.

The protocol preserves this distinction.

---

# Repository Structure

```text
schemas/
  causality-link-record.schema.json
  delegation-causality-chain.schema.json

examples/
  causality-link-record.example.yaml
  delegation-causality-chain.example.yaml

scripts/
  validate_examples.py

docs/
  causality-link-record.md
  delegation-causality-chain.md
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

[success] all examples are valid
```

---

# Roadmap

## v0.1 — Causality Link Record

Define an atomic evidence-backed relationship between a cause event and an effect event.

## v0.2 — Delegation Causality Chain

Trace root intent, task delegation, authority scope, constraint inheritance, redelegation, and result return.

## v0.3 — Action-to-Artifact Binding

Connect action receipts and transformation events to generated artifacts.

## v0.4 — Contribution Causality Graph

Represent multi-source causal contribution structures without prematurely converting them into financial allocations.

## v0.5 — Unified Causality Lifecycle

Connect questions, traces, delegation, actions, transformations, artifacts, audits, contribution assessment, and royalty readiness.

---

# Design Position

The protocol is intended to sit between:

```text
Trace Systems
      ↓
Causality Layer
      ↓
Agent Delegation
      ↓
Action Receipts
      ↓
Artifact Provenance
      ↓
Audit Systems
      ↓
Contribution Assessment
      ↓
Royalty Systems
```

It does not attempt to replace all of these systems.

Its role is to connect them through explicit causal and delegation relationships.

---

# Philosophy

Complex AI outcomes rarely emerge from one isolated cause.

An artifact may involve:

* a human question;
* an origin trace;
* multiple agents;
* multiple delegation steps;
* external tools;
* retrieved sources;
* transformation processes;
* human selection;
* review and correction.

The purpose of the Trace Causality Chain Protocol is not to pretend that this complexity can always be reduced to one owner or one cause.

Its purpose is to preserve the chain.

A future AI civilization will require more than action logs.

It will require the ability to answer:

> Where did this begin?

> Who inherited the task?

> What authority did they receive?

> What constraints were preserved?

> What changed along the way?

> Which actions produced the final artifact?

The Trace Causality Chain Protocol begins building that answer one link and one delegation at a time.

## Status

Experimental specification.

Current version: **v0.2**

The protocol is under active structural development.

