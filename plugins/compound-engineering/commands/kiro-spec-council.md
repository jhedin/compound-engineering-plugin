---
name: kiro-spec-council
description: Run a council of agents to review a spec in parallel
argument-hint: "[spec folder path, e.g., .claude/specs/auth-feature]"
---

# Kiro Spec Council

Review a spec using multiple specialized agents in parallel.

## Input

<spec_path> #$ARGUMENTS </spec_path>

If no path provided, list available specs and ask user to choose.

## Workflow

### 1. Load Spec Files

Read all files from the spec folder:
- `requirements.md`
- `design.md`
- `tasks.md` (if exists)

Combine into a single context for the agents.

### 2. Run Council (Parallel)

Launch ALL three agents simultaneously using the Task tool:

```
Task spec-flow-analyzer: Analyze the spec for user flow completeness. Identify all user journeys, edge cases, and gaps in the specification. Focus on what happens from the user's perspective.

Task architecture-strategist: Review the design document for architectural soundness. Check component boundaries, data flow, error handling strategy, and alignment with requirements.

Task requirements-analyst: Review the requirements document for EARS format compliance and quality. Check that acceptance criteria are testable, specific, and complete.
```

### 3. Synthesize Findings

After all agents complete, consolidate their findings:

1. **Collect** all findings from the three agents
2. **Deduplicate** - Remove overlapping issues found by multiple agents
3. **Categorize** by type:
   - Requirements issues
   - Design issues
   - Architecture issues
   - User flow gaps
4. **Prioritize** by severity:
   - P1 (Critical) - Blocks implementation or creates risk
   - P2 (Important) - Should fix for quality
   - P3 (Nice-to-have) - Improvements

### 4. Present Summary

```markdown
## Spec Review Complete

**Spec:** {spec-name}
**Reviewed by:** spec-flow-analyzer, architecture-strategist, requirements-analyst

### Findings Summary
- **Total Issues:** {count}
- **P1 Critical:** {count}
- **P2 Important:** {count}
- **P3 Nice-to-have:** {count}

### By Category

**Requirements ({count}):**
- {finding with priority}
- {finding with priority}

**Design ({count}):**
- {finding with priority}

**Architecture ({count}):**
- {finding with priority}

**User Flows ({count}):**
- {finding with priority}

### P1 Critical Issues (Address Before Implementation)

1. {issue description}
   - **Found by:** {agent}
   - **Impact:** {why this matters}
   - **Recommendation:** {how to fix}

2. {issue description}
   ...

### Recommended Next Steps

1. Address all P1 issues before proceeding
2. Consider P2 issues during implementation
3. P3 items can be addressed as enhancements

### Agent Reports

<details>
<summary>spec-flow-analyzer full report</summary>
{agent output}
</details>

<details>
<summary>architecture-strategist full report</summary>
{agent output}
</details>

<details>
<summary>requirements-analyst full report</summary>
{agent output}
</details>
```

## Usage Examples

**Review a specific spec:**
```
/kiro-spec-council .claude/specs/user-auth
```

**Review after creating a spec:**
```
/kiro-spec "add payment processing"
... (spec created) ...
/kiro-spec-council .claude/specs/payment-processing
```

## When to Use This Command

- After creating a spec with `/kiro-spec` and before implementation
- When you want multiple perspectives on a spec
- Before starting a large feature to catch issues early
- When reviewing someone else's spec document
