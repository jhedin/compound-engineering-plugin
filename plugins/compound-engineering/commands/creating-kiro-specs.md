---
name: creating-kiro-specs
description: Create a structured spec with requirements, design, and tasks
argument-hint: "[feature description, e.g., 'add user authentication']"
---

# Kiro Spec

Create a structured specification for a feature using the creating-kiro-specs skill.

## Input

<feature> #$ARGUMENTS </feature>

If no feature description provided, ask the user what feature they want to spec out.

## Instructions

Follow the creating-kiro-specs skill workflow exactly:

1. **Phase 1: Requirements** - Generate requirements.md in EARS format, then ask for approval
2. **Phase 2: Design** - After approval, generate design.md with architecture, then ask for approval
3. **Phase 3: Tasks** - After approval, generate tasks.md with implementation checklist

Output goes to `.claude/specs/{feature-name}/`

Key rules:
- Generate first, ask questions later (make reasonable assumptions)
- Explicit approval gates between each phase
- Present summaries, not full documents
- Never auto-proceed to next phase

After completion, suggest `/executing-kiro-tasks` to begin implementation.
