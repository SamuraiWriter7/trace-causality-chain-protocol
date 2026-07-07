# Delegation Causality Chain

## Purpose

The Delegation Causality Chain records how an originating intent moves through a sequence of humans, AI agents, sub-agents, systems, and tools.

Its purpose is to preserve the lineage of delegated work.

A simple delegation chain may look like:

```text
Human
  ↓
Agent A
  ↓
Agent B
  ↓
Tool
```

However, real agent systems are more complex.

Each delegation may change:

* task scope;
* authority;
* permissions;
* constraints;
* delegation depth;
* expected outputs;
* responsibility boundaries.

The Delegation Causality Chain makes these changes explicit.

## Root Intent

Every chain begins with a root intent.

The root intent identifies:

* who initiated the work;
* what question or trace motivated the work;
* what the original objective was.

Conceptually:

```text
Question
   ↓
Trace
   ↓
Root Intent
   ↓
Delegation Chain
```

The root intent allows downstream activity to remain connected to its originating context.

Without this connection, a sequence of technically valid actions may lose the purpose that justified them.

## Participants

A delegation chain may include:

* humans;
* agents;
* sub-agents;
* systems;
* tools;
* organizations;
* other actors.

Each participant has a stable identifier within the chain.

The protocol does not require a universal identity system.

External identity, authentication, or authorization systems may be referenced separately.

## Delegation Steps

Each delegation step records a transfer of task responsibility or execution responsibility.

A step identifies:

* delegator;
* delegatee;
* task;
* delegation type;
* authority scope;
* constraint inheritance;
* parent delegation step;
* status;
* time;
* optional result references.

A chain may therefore reconstruct not only who acted, but how responsibility moved.

## Delegation Types

v0.2 supports:

### `human_to_agent`

A human delegates work to an AI agent.

### `agent_to_agent`

One peer-level agent delegates work to another agent.

### `agent_to_sub_agent`

An agent creates or invokes a subordinate execution relationship.

### `agent_to_tool`

An agent invokes a tool or external execution mechanism.

### `system_to_agent`

A system-level orchestrator assigns work to an agent.

### `handoff`

Responsibility or context is transferred between participants.

### `result_return`

A result moves back toward an upstream participant.

### `other`

The delegation relationship does not fit the predefined classes.

## Authority Scope

Delegation should not imply unlimited authority.

Each step may define:

```text
Allowed Actions
Prohibited Actions
Redelegation Permission
Maximum Delegation Depth
```

For example:

```text
Agent A
  may:
    analyze
    classify
    summarize

  may not:
    publish
    approve payment
    modify ownership records
```

Authority should be explicit whenever downstream agents could take consequential actions.

## Constraint Inheritance

Delegated work often carries constraints.

Examples include:

* preserve uncertainty;
* do not publish automatically;
* require human review;
* do not assign legal ownership;
* do not modify source records.

When work is redelegated, those constraints may be:

* strictly inherited;
* preserved with bounded additions;
* explicitly overridden;
* not inherited.

The protocol records this behavior through `constraint_policy`.

## Inheritance Modes

### `strict`

All inherited constraints remain active.

No inherited constraint should be silently removed.

### `bounded_extension`

Inherited constraints remain active, while additional downstream constraints may be added.

### `explicit_override`

A downstream step may modify inherited constraints, but the modification should be visible and justified.

### `none`

No constraint inheritance is claimed.

This mode should be used carefully in chains involving consequential actions.

## Parent Step Relationships

A delegation step may reference its parent step.

This allows the chain to express branching structures.

Example:

```text
Human
  ↓
Agent A
  ├──→ Agent B
  ├──→ Agent C
  └──→ Tool D
```

The resulting structure is no longer merely a linear log.

It becomes a delegation lineage graph.

v0.2 records the building blocks required for such graphs while keeping the representation simple.

## Relationship to Causality Link Record

The v0.1 Causality Link Record and v0.2 Delegation Causality Chain serve different purposes.

The Causality Link Record asks:

> What relationship exists between Event A and Event B?

The Delegation Causality Chain asks:

> How did responsibility, task scope, authority, and constraints move across participants?

A delegation chain may reference one or more Causality Link Records.

Conceptually:

```text
Causality Link
      ↓
Delegation Step
      ↓
Delegation Chain
```

The protocol intentionally keeps these records separate.

Delegation does not automatically prove that every downstream artifact was caused exclusively by the original delegator.

## Non-Goals of v0.2

Version 0.2 does not attempt to:

* authenticate participant identity;
* issue cryptographic credentials;
* calculate royalties;
* determine legal responsibility;
* prove exclusive authorship;
* automatically resolve authority disputes;
* bind every action to a final artifact.

Action-to-artifact binding is reserved for v0.3.

## Future Direction

The protocol roadmap is:

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

v0.2 establishes the delegation spine required for later versions.

The central principle is simple:

> An agent action should not exist as an isolated event when it was produced through a chain of inherited intent, authority, and constraints.
