# Trace Causality Chain Protocol

An open protocol for recording and connecting causal links from human questions and origin traces through agent delegation, actions, transformations, artifacts, contribution graphs, audits, royalty readiness, and human review.

## Overview

AI-era artifacts increasingly emerge from distributed causal processes.

A human may ask the original question.

That question may become a persistent trace.

An AI agent may inherit the trace.

Work may be delegated to multiple agents.

Tools may execute calculations or validations.

Actions may generate or transform artifact fragments.

Multiple contributions may branch and converge.

The resulting contribution structure may be audited.

Only after those stages should a system evaluate whether the record is ready for downstream royalty or value-allocation policy.

The Trace Causality Chain Protocol makes this lifecycle machine-readable.

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

---

# Protocol Layers

## v0.1 — Causality Link Record

Defines an atomic evidence-backed relationship between two events.

```text
Cause Event
     ↓
Effect Event
```

The record distinguishes:

* direct causation;
* contributing causation;
* enabling conditions;
* transformation;
* delegation;
* influence;
* temporal precedence;
* structural similarity;
* independent convergence.

The central principle is:

> Similarity, chronology, influence, and causation should not be treated as the same thing.

---

## v0.2 — Delegation Causality Chain

Records how intent, tasks, authority, and constraints move through humans, agents, sub-agents, systems, and tools.

```text
Human
  ↓
Agent
  ↓
Sub-Agent
  ↓
Tool
```

The protocol records:

* root intent;
* delegator;
* delegatee;
* delegated task;
* authority scope;
* allowed actions;
* prohibited actions;
* redelegation permission;
* delegation depth;
* inherited constraints;
* constraint changes.

The central principle is:

> Delegation is not unlimited authority.

---

## v0.3 — Action-to-Artifact Binding

Connects actions and transformation chains to artifacts or artifact fragments.

```text
Action
   ↓
Transformation
   ↓
Artifact Fragment
```

Bindings may represent:

* generation;
* transformation;
* assembly;
* editing;
* selection;
* verification;
* annotation;
* rejection.

Contribution scopes may identify:

* whole artifacts;
* sections;
* files;
* JSON Pointers;
* line ranges;
* byte ranges;
* time ranges;
* custom regions.

The central principle is:

> Artifact-level attribution is often too coarse.

---

## v0.4 — Contribution Causality Graph

Combines multiple contribution records into an evidence-backed causal graph.

```text
Origin Trace
     │
     ├────→ Agent Analysis ────┐
     │                         │
     ├────→ Tool Execution ────┼──→ Synthesis
     │                         │
     └────→ Context Input ─────┘
               ↓
          Human Selection
               ↓
            Editing
               ↓
          Verification
```

The graph includes:

* contributors;
* contribution nodes;
* causal edges;
* artifact scopes;
* causal roles;
* materiality;
* node confidence;
* edge confidence;
* graph policy;
* graph-level review.

The central principle is:

> Contribution causality is not the same as financial allocation.

---

## v0.5 — Unified Causality Lifecycle

Connects the earlier protocol layers into one lifecycle-level record.

```text
Question
   ↓
Trace
   ↓
Causality Link
   ↓
Delegation Chain
   ↓
Action Receipt
   ↓
Artifact Binding
   ↓
Contribution Graph
   ↓
Audit Bridge
   ↓
Royalty Readiness
   ↓
Human Gate
```

The Unified Causality Lifecycle is reference-oriented.

It does not duplicate every underlying record inside one large document.

Instead, it preserves:

* lifecycle stages;
* record references;
* lifecycle links;
* evidence;
* link confidence;
* audit state;
* blocking conditions;
* readiness checks;
* human-gate status.

---

# Core Principles

## Evidence Before Attribution

Causal and contribution claims should reference inspectable evidence.

## Similarity Is Not Causation

Structural similarity and temporal precedence should not automatically become claims of derivation.

## Delegation Is Not Unlimited Authority

Agent delegation should preserve visible permission and constraint boundaries.

## Contribution Is Multi-Form

Generation is not the only meaningful contribution.

Analysis, selection, editing, orchestration, verification, and contextual input may all participate in causal formation.

## Nodes and Relationships Have Separate Confidence

The existence of an event may be certain while its causal relationship to another event remains uncertain.

## Contribution Is Not Allocation

A causal graph is evidence for later economic evaluation.

It is not itself a royalty table.

## Audit Is a Bridge

Audit may produce:

* pass;
* pass with conditions;
* fail;
* dispute;
* blocking conditions.

Audit is not merely ceremonial validation.

## Human Review Remains Explicit

Machine-readable evidence does not remove the need for human judgment in consequential decisions.

---

# Unified Lifecycle Architecture

```text
┌──────────────────────┐
│ Human Question       │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Trace                │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Causality Link       │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Delegation Chain     │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Action Receipts      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Artifact Bindings    │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Contribution Graph   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Audit Bridge         │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Royalty Readiness    │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Human Gate           │
└──────────────────────┘
```

---

# Allocation Boundary

The protocol intentionally stops before financial allocation.

```text
Causality
   ↓
Contribution
   ↓
Audit
   ↓
Royalty Readiness
   ↓
Human Gate

====== Boundary ======

   ↓
Allocation Policy
   ↓
Contract Evaluation
   ↓
Settlement
   ↓
Royalty Distribution
```

The Unified Causality Lifecycle requires:

```text
financial_allocation_executed: false
```

This preserves separation between:

```text
Causality
≠
Contribution
≠
Value
≠
Rights
≠
Allocation
≠
Payment
```

---

# Audit Bridge

The Audit Bridge records:

* audit status;
* audit references;
* findings;
* blocking conditions;
* proceed permission.

Possible states include:

* `not_requested`
* `pending`
* `passed`
* `passed_with_conditions`
* `failed`
* `disputed`

This allows realistic intermediate states.

For example:

```text
Contribution Graph: valid
Audit: passed with conditions
Rights Review: pending
Proceed to policy evaluation: allowed
```

---

# Royalty Readiness

Royalty Readiness does not calculate payments.

It evaluates whether the causal record is sufficiently mature for external allocation policy evaluation.

Possible checks include:

* provenance completeness;
* contribution graph validity;
* audit completion;
* rights review;
* dispute resolution;
* human approval requirements.

Possible readiness states are:

* `not_assessed`
* `not_ready`
* `conditionally_ready`
* `ready`
* `blocked`
* `disputed`

---

# Human Gate

The Human Gate records the final lifecycle decision before downstream allocation systems may proceed.

Possible states include:

* `not_required`
* `pending`
* `approved`
* `approved_with_conditions`
* `rejected`
* `deferred`
* `disputed`

The gate may contain:

* reviewer references;
* decision timestamp;
* conditions;
* decision basis.

---

# Validation

The protocol uses multiple validation layers.

## Schema Validation

Validates JSON Schema conformance.

## Contribution Graph Validation

Checks:

* contributor references;
* node references;
* artifact references;
* identifier uniqueness;
* self-loops;
* cycles;
* root policies;
* parent policies.

## Unified Lifecycle Validation

Checks:

* Stage ID uniqueness;
* sequence uniqueness;
* Link ID uniqueness;
* required lifecycle stages;
* valid Stage references;
* canonical stage ordering;
* self-loops;
* complete path from Question to Human Gate;
* Audit Bridge consistency;
* allocation boundary preservation.

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

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

[validate] Contribution Causality Graph
[ok] contribution-causality-graph.example.yaml is valid

[validate] Unified Causality Lifecycle
[ok] unified-causality-lifecycle.example.yaml is valid

[success] all examples are valid
```

---

# Repository Structure

```text
schemas/
  causality-link-record.schema.json
  delegation-causality-chain.schema.json
  action-artifact-binding.schema.json
  contribution-causality-graph.schema.json
  unified-causality-lifecycle.schema.json

examples/
  causality-link-record.example.yaml
  delegation-causality-chain.example.yaml
  action-artifact-binding.example.yaml
  contribution-causality-graph.example.yaml
  unified-causality-lifecycle.example.yaml

docs/
  causality-link-record.md
  delegation-causality-chain.md
  action-to-artifact-binding.md
  contribution-causality-graph.md
  unified-causality-lifecycle.md

scripts/
  validate_examples.py
```

---

# Version Arc

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

The first protocol arc is complete at v0.5.

---

# Design Position

The Trace Causality Chain Protocol is a connective layer.

It does not replace:

* Trace systems;
* Agent communication protocols;
* Delegation systems;
* Action Receipt systems;
* Artifact provenance systems;
* Audit protocols;
* Rights systems;
* Royalty policy systems;
* Settlement infrastructure.

Its purpose is to connect them through explicit, evidence-backed causal relationships.

```text
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
Contribution
  ↓
Audit
  ↓
Readiness
```

---

# Philosophy

A final artifact is only the visible surface of a deeper causal structure.

Behind it may exist:

* an originating human question;
* persistent traces;
* inherited context;
* agent delegation;
* sub-agent analysis;
* tool execution;
* transformation;
* selection;
* rejection;
* editing;
* verification;
* audit;
* human judgment.

The protocol attempts to preserve this hidden structure.

Before asking:

> Who owns this?

Before asking:

> Who should receive value?

Before asking:

> What percentage should be allocated?

a system should first be able to answer:

> Where did this begin?

> What traces were inherited?

> Who delegated the work?

> What authority was transferred?

> What actions occurred?

> Which artifact regions were affected?

> How did contributions combine?

> What evidence supports each relationship?

> What uncertainties remain?

> Has the structure been audited?

> Is it ready for downstream allocation policy evaluation?

The Trace Causality Chain Protocol exists to make these questions machine-readable without pretending that causality, contribution, rights, value, and payment are the same thing.

## Status

Experimental specification.

Current version: **v0.5**

First protocol arc complete.

