---
name: agent-native-architecture
description: Design applications where agents are first-class citizens
argument-hint: "[feature or system to design]"
---

# Agent-Native Architecture

Design applications where AI agents are first-class citizens.

## Input

<design_request> #$ARGUMENTS </design_request>

## Instructions

Follow the agent-native-architecture skill to ensure:

- **Action parity** - Anything a user can do, an agent can do
- **Context parity** - Anything a user can see, an agent can see
- **Tool primitives** - Features exposed as composable tools
- **Self-modifying** - Systems that can improve themselves
- **Loop-friendly** - Designed for autonomous agent operation

## Key Principles

1. Every UI action has an API/tool equivalent
2. State is observable and queryable
3. Operations are idempotent where possible
4. Errors are informative and recoverable
5. Permissions work for both humans and agents

## Example

```
/agent-native-architecture design an email management system
/agent-native-architecture review the checkout flow for agent compatibility
```

## See Also

- `/agent-native-audit` - Audit existing code for agent-native compliance
