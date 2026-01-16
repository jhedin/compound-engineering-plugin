---
name: reviewing-kiro-specs
description: Review a Kiro spec for completeness and quality
argument-hint: "[spec folder path, e.g., .claude/specs/auth-feature]"
---

# Kiro Spec Review

Review a spec created by the creating-kiro-specs skill for completeness and quality.

## Input

<spec_path> #$ARGUMENTS </spec_path>

If no path provided, list available specs in `.claude/specs/` and ask user to choose.

## Workflow

### 1. Load Spec Files

Read all files from the spec folder:
- `requirements.md`
- `design.md`
- `tasks.md` (if exists)

### 2. Review the Spec

Analyze the spec for:

**Requirements Quality:**
- EARS format compliance (ubiquitous, event-driven, state-driven, optional feature, unwanted behavior)
- Testable acceptance criteria
- Clear scope boundaries (what's in/out)
- Edge cases and error scenarios

**Design Soundness:**
- Architecture alignment with requirements
- Component boundaries and interfaces
- Data model completeness
- Error handling strategy
- Testing strategy coverage

**Task Completeness:**
- All requirements have corresponding tasks
- Tasks are ordered for incremental implementation
- TDD approach where appropriate
- No non-coding tasks (deployment, docs, etc.)

### 3. Present Findings

Summarize issues by priority:
- **P1 (Critical)** - Blocks implementation or creates risk
- **P2 (Important)** - Should fix for quality
- **P3 (Nice-to-have)** - Improvements

Include specific recommendations for each issue.

## Usage

```
/reviewing-kiro-specs .claude/specs/user-auth
```

## For Multi-Agent Review

To run multiple specialized reviewers in parallel, use `/plan_review` instead:

```
/plan_review .claude/specs/user-auth
```

This will launch spec-flow-analyzer, architecture-strategist, and other agents simultaneously.
