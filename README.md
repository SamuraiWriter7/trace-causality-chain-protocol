# Trace Causality Chain Protocol

An open protocol for recording causal links from human questions and origin traces through agent delegation, actions, transformations, artifacts, audits, and royalty readiness.

## Overview

AI systems increasingly operate through chains of interactions rather than isolated prompts and responses.

A human question may create a trace.

That trace may be inherited by an AI agent.

The agent may delegate work to another agent.

Several actions and transformations may produce an artifact.

The artifact may later be audited, reused, transformed, or connected to economic value.

However, most current records describe individual events:

* a trace was created;
* an agent acted;
* a task was delegated;
* an artifact was produced;
* an audit was performed.

What is often missing is the relationship between them.

The Trace Causality Chain Protocol addresses this gap by defining machine-readable records for expressing evidence-backed causal relationships between events.

The protocol does not assume that chronological order proves causation.

It distinguishes between:

* direct causation;
* contributing causes;
* enabling conditions;
* transformation;
* delegation;
* influence;
* temporal precedence;
* structural similarity;
* independent convergence;
* unknown relationships.

This distinction is central to the protocol.

## Core Principle

> Record causal claims as reviewable, evidence-backed relationships rather than unquestionable facts.

The protocol is designed to preserve uncertainty.

A causality record may express:

* what event is considered the cause;
* what event is considered the effect;
* what kind of relationship is claimed;
* what evidence supports that relationship;
* how confident the assessment is;
* whether human review is required;
* whether the claim has been confirmed, rejected, or disputed.

## v0.1 — Causality Link Record

Version 0.1 introduces the smallest unit of the protocol:

**Causality Link Record**

A Causality Link Record connects one cause event with one effect event.

Conceptually:

```text
Cause Event
     │
     │ evidence-backed relation
     ▼
Effect Event
```

Example:

```text
Human Question
     ↓
Trace
     ↓
Artifact
```

Each individual connection can be recorded independently.

Future versions may combine these links into longer causal chains and contribution graphs.

## Event Types

v0.1 supports references to events including:

* question;
* trace;
* delegation;
* agent action;
* transformation;
* artifact;
* audit;
* contribution;
* allocation;
* other event types.

The protocol stores references rather than requiring every external record format to be embedded directly.

This allows the protocol to connect with independent Trace, Action Receipt, Agent Handoff, Audit, and Royalty systems.

## Relation Types

A causal relationship must not be reduced to a simple binary claim.

v0.1 defines the following relation types:

### `direct_cause`

The cause event is assessed as directly producing the effect event.

### `contributing_cause`

The cause event materially contributed to the effect but was not necessarily sufficient or exclusive.

### `enabling_condition`

The cause event created conditions that made the effect possible.

### `transformation`

The effect is a transformed form or derivative development of the cause.

### `delegation`

The effect occurred through an explicit transfer of responsibility or task authority.

### `influence`

The cause appears to have influenced the effect, but stronger causal attribution is not established.

### `temporal_precedence`

The cause event occurred before the effect event, but causality has not been established.

### `structural_similarity`

The events share notable structural characteristics, without asserting direct influence.

### `independent_convergence`

Similar structures appear to have emerged independently.

### `unknown`

The relationship cannot yet be classified.

## Evidence Before Attribution

The protocol requires at least one evidence reference.

Evidence may include:

* trace records;
* action receipts;
* handoff records;
* artifacts;
* audit records;
* external sources;
* human testimony;
* other relevant records.

A record is therefore not merely a statement that:

> A caused B.

Instead, it expresses:

> Based on the referenced evidence, A is assessed as having this kind of relationship to B, with this degree of confidence and this review state.

## Confidence and Review

Every record contains a causality confidence assessment.

The confidence score ranges from:

```text
0.0 → no confidence

1.0 → maximum confidence
```

The score must include a textual basis explaining why it was assigned.

Confidence is not a substitute for evidence.

Human review states are separately recorded.

Supported review states include:

* unreviewed;
* machine assessed;
* human review required;
* human confirmed;
* human rejected;
* disputed.

This separation allows AI systems to propose causal connections without automatically turning those proposals into authoritative claims.

## Design Position

The Trace Causality Chain Protocol is intended to sit between existing trace systems and downstream value systems.

```text
Question
   ↓
Trace
   ↓
Causality Chain
   ↓
Delegation
   ↓
Action
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

v0.1 does not implement this full lifecycle.

It establishes the atomic causal link required to build it.

## Repository Structure

```text
schemas/
  causality-link-record.schema.json

examples/
  causality-link-record.example.yaml

scripts/
  validate_examples.py

docs/
  causality-link-record.md
```

## Validation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run validation:

```bash
python scripts/validate_examples.py
```

## Roadmap

### v0.1 — Causality Link Record

Define the atomic evidence-backed relationship between a cause event and an effect event.

### v0.2 — Delegation Causality Chain

Connect human delegation, agent handoffs, sub-agent execution, and tool use into traceable causal sequences.

### v0.3 — Action-to-Artifact Binding

Connect action receipts and transformation records to generated artifacts.

### v0.4 — Contribution Causality Graph

Represent multi-source contribution structures without prematurely converting them into financial allocations.

### v0.5 — Unified Causality Lifecycle

Connect questions, traces, delegation, actions, transformations, artifacts, audits, contribution assessment, and royalty readiness.

## Philosophy

Complex outcomes rarely have only one cause.

AI-generated artifacts may emerge from combinations of:

* human questions;
* previous traces;
* model behavior;
* agent delegation;
* tool output;
* external sources;
* human selection;
* structural transformation.

The purpose of this protocol is not to manufacture certainty.

Its purpose is to make causal claims:

**visible, inspectable, reviewable, disputable, and interoperable.**

## Status

Experimental specification.

Current version: **v0.1**

The protocol is under active structural development.
