
# Trace Causality Chain Protocol

An open protocol for recording causal links from human questions and origin traces through agent delegation, actions, transformations, artifacts, audits, contribution graphs, and royalty readiness.

## Overview

AI-era artifacts increasingly emerge from distributed chains of human questions, traces, agent delegation, analysis, generation, tool execution, transformation, selection, editing, and verification.

A final artifact may contain contributions from:

* a human originator;
* one or more AI agents;
* sub-agents;
* external tools;
* retrieved sources;
* transformation processes;
* human selection;
* human editing;
* automated verification.

The Trace Causality Chain Protocol provides machine-readable records for preserving the causal relationships across this lifecycle.

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
Transformation
   ↓
Artifact Binding
   ↓
Contribution Graph
   ↓
Audit
   ↓
Royalty Readiness
```

The protocol develops this structure incrementally.

---

## Core Principles

### Evidence Before Attribution

Causal claims and contribution claims should reference inspectable evidence.

### Similarity Is Not Causation

Temporal precedence, structural similarity, influence, contribution, direct causation, and independent convergence remain distinct.

### Delegation Is Not Unlimited Authority

Delegation may carry explicit permissions, prohibitions, redelegation rules, depth limits, and inherited constraints.

### Constraints Should Survive Delegation

When tasks move through multi-agent systems, inherited constraints should remain visible.

### Artifacts Are Composed of Contributions

An action may contribute to an entire artifact or only to a specific artifact fragment.

### Generation Is Not the Only Contribution

Analysis, transformation, selection, editing, orchestration, verification, annotation, rejection, and contextual input may all be causally relevant.

### Graphs Should Preserve Uncertainty

Contribution nodes and causal edges carry independent confidence assessments.

### Contribution Is Not Allocation

A contribution graph should not automatically become a financial allocation table.

---

# v0.1 — Causality Link Record

Version 0.1 introduced the atomic causal relationship:

```text
Cause Event
     ↓
Effect Event
```

A record contains:

* cause event;
* effect event;
* relation type;
* evidence references;
* causality confidence;
* review status.

Supported relationships include:

* direct cause;
* contributing cause;
* enabling condition;
* transformation;
* delegation;
* influence;
* temporal precedence;
* structural similarity;
* independent convergence;
* unknown.

The purpose is to record causal claims as evidence-backed and reviewable assessments.

---

# v0.2 — Delegation Causality Chain

Version 0.2 introduced structured delegation lineage.

```text
Human
  ↓
Agent
  ↓
Sub-Agent
  ↓
Tool
```

Each chain may record:

* root intent;
* participants;
* delegated tasks;
* delegator and delegatee relationships;
* authority scope;
* allowed actions;
* prohibited actions;
* redelegation permission;
* maximum delegation depth;
* inherited constraints;
* parent delegation steps;
* result references.

The central principle is:

> Delegation should preserve visible responsibility and constraint lineage.

---

# v0.3 — Action-to-Artifact Binding

Version 0.3 connected actions to artifacts or artifact fragments.

```text
Action
   ↓
Transformation
   ↓
Artifact Fragment
```

A binding may identify:

* action reference;
* artifact reference;
* binding type;
* contribution scope;
* transformation chain;
* evidence;
* binding confidence;
* verification status.

Supported binding types include:

* generated;
* transformed;
* assembled;
* edited;
* selected;
* verified;
* annotated;
* rejected;
* other.

Supported artifact scopes include:

* whole artifact;
* section;
* file;
* JSON Pointer;
* line range;
* byte range;
* time range;
* custom scope.

v0.3 establishes the principle that artifact-level attribution is often too coarse.

---

# v0.4 — Contribution Causality Graph

Version 0.4 combines individual contribution records into graph-level causal structures.

A graph may represent:

```text
Human Question
      ↓
Origin Trace
      │
      ├────→ Agent Analysis ────┐
      │                         │
      └────→ Tool Execution ────┼──→ Synthesis
                                │
External Context ───────────────┘
             ↓
       Human Selection
             ↓
         Human Edit
             ↓
        Verification
```

The Contribution Causality Graph contains:

* artifact references;
* contributor records;
* contribution nodes;
* causal edges;
* contribution scopes;
* causal roles;
* materiality assessments;
* node confidence;
* edge confidence;
* graph policy;
* graph-level confidence;
* human review status.

## Contribution Nodes

Supported contribution types include:

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

## Causal Roles

Supported causal roles include:

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

## Materiality

v0.4 uses ordinal materiality:

* `critical`
* `major`
* `moderate`
* `minor`
* `undetermined`

Materiality is not a financial percentage.

A critical causal contribution does not automatically receive a fixed royalty share.

## Edge Relationships

Supported relationships include:

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

## Node Confidence and Edge Confidence

Contribution event confidence and causal relationship confidence are separate.

```text
Node Confidence
       ≠
Edge Confidence
```

A system may know with high confidence that an action occurred while remaining uncertain about its exact causal influence on a final artifact.

v0.4 preserves this distinction.

## Contribution Graph Is Not Allocation Graph

The protocol intentionally separates:

```text
Causality
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

v0.4 stops before financial allocation.

The protocol does not infer ownership, copyright, or payment percentage from a causal graph alone.

---

# Semantic Graph Validation

v0.4 extends validation beyond JSON Schema conformance.

The validator checks:

* duplicate contributor IDs;
* duplicate node IDs;
* duplicate edge IDs;
* invalid contributor references;
* invalid artifact references;
* invalid node references;
* self-loops;
* multiple roots when prohibited;
* multiple parents when prohibited;
* cycles when acyclic structure is expected.

This establishes two validation layers:

```text
Schema Validation
        +
Semantic Graph Validation
```

---

# Relationship Between Versions

```text
v0.1
Causality Link
     ↓
v0.2
Delegation Chain
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

Each version asks a different question.

### v0.1

What event relates to what event?

### v0.2

Who delegated what to whom, under what authority and constraints?

### v0.3

Which action contributed to which artifact or artifact fragment?

### v0.4

How do multiple contributions branch, transform, and converge?

### v0.5

How does the full lifecycle connect from originating question to audit and royalty readiness?

---

# Repository Structure

```text
schemas/
  causality-link-record.schema.json
  delegation-causality-chain.schema.json
  action-artifact-binding.schema.json
  contribution-causality-graph.schema.json

examples/
  causality-link-record.example.yaml
  delegation-causality-chain.example.yaml
  action-artifact-binding.example.yaml
  contribution-causality-graph.example.yaml

docs/
  causality-link-record.md
  delegation-causality-chain.md
  action-to-artifact-binding.md
  contribution-causality-graph.md

scripts/
  validate_examples.py
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

[validate] Contribution Causality Graph
[ok] contribution-causality-graph.example.yaml is valid

[success] all examples are valid
```

---

# Roadmap

## v0.1 — Causality Link Record

Atomic evidence-backed event relationships.

## v0.2 — Delegation Causality Chain

Root intent, delegation lineage, authority scope, and constraint inheritance.

## v0.3 — Action-to-Artifact Binding

Action and transformation binding to artifacts and artifact fragments.

## v0.4 — Contribution Causality Graph

Graph-level representation of branching, converging, and transforming contributions.

## v0.5 — Unified Causality Lifecycle

Unified lifecycle connecting:

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
Royalty Readiness
↓
Human Gate
```

---

# Design Position

The Trace Causality Chain Protocol is a connective causality layer.

It does not attempt to replace:

* trace systems;
* task protocols;
* agent communication protocols;
* tool execution systems;
* provenance systems;
* audit systems;
* legal systems;
* royalty systems.

Its role is to preserve the causal paths connecting them.

```text
Trace Systems
      ↓
Causality Records
      ↓
Delegation Chains
      ↓
Action Receipts
      ↓
Artifact Bindings
      ↓
Contribution Graphs
      ↓
Audit
      ↓
Royalty Readiness
```

---

# Philosophy

A complex artifact rarely emerges from one isolated cause.

A future AI-generated work may involve:

* a human asking the original question;
* another human preserving the trace;
* an agent performing research;
* another agent synthesizing the research;
* a tool performing calculation;
* a human selecting one path;
* another agent rewriting the structure;
* a human correcting the result;
* a machine verifying conformance.

The final artifact is not merely a file.

It is the visible surface of a hidden causal structure.

The purpose of this protocol is to make that structure inspectable.

Before asking:

> Who owns this?

Before asking:

> Who should be paid?

Before asking:

> What percentage belongs to whom?

the system should first ask:

> What happened?

> Who contributed?

> Where did the contribution enter?

> How did contributions combine?

> What was transformed?

> What was selected?

> What was rejected?

> What was verified?

> What evidence supports each relationship?

Trace Causality Chain Protocol attempts to preserve these answers without pretending that causality, value, ownership, and payment are the same thing.

## Status

Experimental specification.

Current version: **v0.4**

The protocol is under active structural development.
