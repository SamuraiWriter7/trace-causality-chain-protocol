# Causality Link Record

## Purpose

The Causality Link Record is the atomic unit of the Trace Causality Chain Protocol.

It represents an assessed relationship between two events:

```text
Cause Event
     ↓
Effect Event
```

The purpose of the record is not to prove causality automatically.

Its purpose is to express a causal hypothesis in a structured form that can be:

* inspected;
* validated;
* reviewed;
* disputed;
* connected to other protocol records.

## Why a Separate Causality Layer Is Needed

Trace systems can record that an idea or question existed.

Action receipt systems can record that an agent performed an action.

Handoff records can record that responsibility moved between agents.

Artifact systems can record that an output was produced.

Audit systems can assess compliance or provenance.

However, these records do not necessarily answer:

> Which earlier event contributed to this later event?

The Causality Link Record provides a minimal bridge between event records.

## Minimal Model

A v0.1 record contains:

```text
Cause Event
Effect Event
Relation Type
Evidence References
Causality Confidence
Review Status
```

The protocol requires evidence references because chronological order alone is insufficient to establish causality.

## Distinguishing Relationship Types

A central design goal is to avoid collapsing all similarity into causation.

The following relationships are intentionally distinct:

```text
Temporal Precedence
≠
Structural Similarity
≠
Influence
≠
Contributing Cause
≠
Direct Cause
```

For example, two systems may share a similar architecture.

This could indicate:

* independent convergence;
* shared external influence;
* structural similarity;
* direct derivation.

The protocol does not force these cases into a single category.

## Confidence Is Not Proof

The `causality_confidence` field records an assessment.

It contains:

* a numerical score from 0 to 1;
* a textual explanation of the basis.

The score should not be interpreted as objective probability unless an external methodology explicitly defines it that way.

The field exists to expose the assessor's level of confidence rather than conceal uncertainty.

## Human Review

Machine-generated causality assessments may be useful for:

* candidate link detection;
* provenance analysis;
* origin audits;
* agent workflow reconstruction.

However, machine assessment should not automatically become authoritative attribution.

The protocol therefore separates:

```text
causality_confidence
```

from:

```text
review_status
```

A system may produce a high-confidence assessment while still requiring human review.

Likewise, a claim may become disputed even after previous confirmation.

## External References

The protocol uses references rather than embedding full external records.

For example:

```yaml
cause_event:
  event_id: trace-001
  event_type: trace
  ref: trace://example/trace-001
```

This approach allows a Causality Link Record to connect with external systems without requiring them to adopt one universal storage model.

Potential integrations include:

* Trace Relay records;
* AI Action Receipts;
* Agent Handoff Records;
* synchronization audit records;
* artifact registries;
* origin structure records;
* contribution graphs;
* Royalty OS readiness records.

## Non-Goals of v0.1

Version 0.1 does not attempt to:

* calculate financial royalties;
* determine legal ownership;
* prove plagiarism;
* establish exclusive authorship;
* automatically resolve disputes;
* construct full multi-hop causality graphs;
* define cryptographic identity infrastructure.

These may be handled by external systems or future versions.

## Example Interpretation

Suppose:

```text
Trace A
   ↓
Artifact B
```

A record with:

```yaml
relation_type: contributing_cause
```

means:

> Available evidence supports the assessment that Trace A materially contributed to Artifact B.

It does not automatically mean:

> Trace A was the only cause of Artifact B.

This distinction is essential for multi-agent and human-AI collaborative environments.

## Future Extension

The atomic link introduced in v0.1 is intended to become the basis for:

```text
Link
 ↓
Chain
 ↓
Graph
 ↓
Contribution Assessment
 ↓
Royalty Readiness
```

The protocol therefore begins with a deliberately small primitive.

A civilization-scale causal graph should not begin by claiming omniscience.

It should begin by recording one carefully qualified relationship at a time.
