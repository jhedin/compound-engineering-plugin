---
name: kiro-spec
description: This skill implements spec-driven development with explicit approval gates. Use when starting a new feature, planning implementation, or when the user wants structured requirements/design/tasks documents. Adapted from Amazon Kiro's spec workflow.
---

# Kiro Spec Workflow

Spec-driven development workflow adapted from Amazon Kiro.

## Overview

This skill creates structured specification documents for features:
- `requirements.md` - EARS format user stories and acceptance criteria
- `design.md` - Architecture, components, data models, testing strategy
- `tasks.md` - TDD-focused implementation checklist

## Output Location

All files go to: `.claude/specs/{feature-name}/`

Create the directory if it doesn't exist. Use kebab-case for the feature name (e.g., `dark-mode-toggle`, `user-authentication`).

## Phase 1: Requirements

Generate requirements document WITHOUT asking sequential questions first. Make reasonable assumptions based on the user's rough idea, then present for feedback.

**Format:** Use EARS format from [ears-format.md](./references/ears-format.md)

**Required sections:**
1. Introduction - Feature summary
2. User Stories - Hierarchical numbered list with acceptance criteria
3. Non-Functional Requirements - Performance, security, accessibility
4. Edge Cases - Error scenarios, boundary conditions
5. Out of Scope - What this feature does NOT include

**After writing requirements.md:**
- Present a summary to user (not the full document)
- Ask: "Do the requirements look good? Let me know if you'd like any changes, or say 'approved' to move on to the design."
- MUST NOT proceed until user explicitly approves ("yes", "approved", "looks good", "lgtm")
- If user requests changes, revise and ask again

## Phase 2: Design

After requirements approval, create design document.

**Required sections:**
- Overview - What we're building and why
- Architecture - High-level system design, components involved
- Components and Interfaces - Detailed component breakdown, APIs, contracts
- Data Models - Database schemas, data structures, state management
- Error Handling - How errors are caught, reported, and recovered
- Testing Strategy - Unit, integration, e2e test approach

**After writing design.md:**
- Present a summary to user
- Ask: "Does the design look good? Let me know if you'd like changes, or say 'approved' to move on to the implementation plan."
- MUST NOT proceed until user explicitly approves
- Offer to return to requirements if gaps are identified

## Phase 3: Tasks

After design approval, create implementation plan.

**Constraints:**
- Format as numbered checkbox list (max 2 levels: 1, 1.1, 1.2, 2, 2.1)
- Each task MUST reference specific requirements (e.g., "Implements requirement 1.2")
- TDD-focused: write tests before implementation where appropriate
- No big jumps in complexity - each task builds incrementally
- ONLY coding tasks - no deployment, user testing, documentation, or non-coding activities
- Each task must be actionable by a coding agent
- Tasks should specify what files or components need to be created/modified

**Example task format:**
```markdown
- [ ] 1. Set up authentication module structure
  - Create `app/services/auth/` directory
  - Implements requirement 1.1
  - [ ] 1.1. Create base authenticator class with interface
  - [ ] 1.2. Write unit tests for authenticator interface
```

**After writing tasks.md:**
- Present task list summary to user
- Ask: "Do the tasks look good? Let me know if you'd like changes, or say 'approved' to complete the spec."
- MUST NOT proceed until user explicitly approves

## Completion

After tasks approved:
- Inform user the spec workflow is complete
- Summarize what was created:
  - `.claude/specs/{feature}/requirements.md`
  - `.claude/specs/{feature}/design.md`
  - `.claude/specs/{feature}/tasks.md`
- Suggest: "You can use `/kiro-task-exec` to begin implementing tasks one at a time, or `/kiro-spec-review` to review the spec for completeness."
- DO NOT begin implementing - that's a separate workflow

## Important Rules

1. **Generate first, ask later** - Don't ask 20 clarifying questions before writing. Make reasonable assumptions and let the user correct.
2. **Explicit approval gates** - MUST wait for clear approval between each phase.
3. **One phase at a time** - Complete requirements before design, design before tasks.
4. **Summaries, not dumps** - Present summaries after writing, not the full document contents.
5. **User controls pace** - Never auto-proceed to the next phase.
