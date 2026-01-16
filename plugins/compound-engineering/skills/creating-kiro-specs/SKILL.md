---
name: creating-kiro-specs
description: This skill creates structured specification documents for features using a three-phase workflow with explicit approval gates. Use when starting a new feature, planning implementation, or when the user wants structured requirements/design/tasks documents. Adapted from Amazon Kiro's spec-driven development workflow.
---

# Kiro Spec

Create structured specification documents through a three-phase workflow with approval gates.

## Quick Start

```
User: "Create a spec for user authentication"

1. Generate requirements.md → Ask for approval
2. Generate design.md → Ask for approval
3. Generate tasks.md → Ask for approval
4. Done - suggest /executing-kiro-tasks to implement
```

Output location: `.claude/specs/{feature-name}/`

## Instructions

### Phase 1: Requirements

Generate requirements document based on the user's rough idea WITHOUT asking sequential questions first. Make reasonable assumptions, then present for feedback.

**Create:** `.claude/specs/{feature-name}/requirements.md`

**Format:** Use EARS (Easy Approach to Requirements Syntax) from [ears-format.md](./references/ears-format.md)

**Required sections:**
1. **Introduction** - Feature summary
2. **User Stories** - Hierarchical numbered list with acceptance criteria
3. **Non-Functional Requirements** - Performance, security, accessibility
4. **Edge Cases** - Error scenarios, boundary conditions
5. **Out of Scope** - What this feature does NOT include

**After writing:**
- Present a summary (not full document)
- Ask: "Do the requirements look good? Let me know if you'd like changes, or say 'approved' to move to design."
- Wait for explicit approval before proceeding

### Phase 2: Design

After requirements approval, create design document with research conducted during the process.

**Create:** `.claude/specs/{feature-name}/design.md`

**Required sections:**
- **Overview** - What we're building and why
- **Architecture** - High-level system design, components involved
- **Components and Interfaces** - Detailed breakdown, APIs, contracts
- **Data Models** - Database schemas, data structures, state management
- **Error Handling** - How errors are caught, reported, recovered
- **Testing Strategy** - Unit, integration, e2e test approach

**After writing:**
- Present a summary
- Ask: "Does the design look good? Let me know if you'd like changes, or say 'approved' to move to tasks."
- Offer to return to requirements if gaps are identified
- Wait for explicit approval before proceeding

### Phase 3: Tasks

After design approval, create implementation plan as a checklist of coding tasks.

**Create:** `.claude/specs/{feature-name}/tasks.md`

**Format constraints:**
- Numbered checkbox list (max 2 levels: 1, 1.1, 1.2, 2, 2.1)
- Each task references specific requirements (e.g., "Implements requirement 1.2")
- TDD-focused: write tests before implementation where appropriate
- No big jumps in complexity - incremental progress
- ONLY coding tasks - no deployment, user testing, documentation

**Task format:**
```markdown
- [ ] 1. Set up authentication module structure
  - Create `app/services/auth/` directory
  - Implements requirement 1.1
  - [ ] 1.1. Create base authenticator class with interface
  - [ ] 1.2. Write unit tests for authenticator interface
```

**After writing:**
- Present task list summary
- Ask: "Do the tasks look good? Let me know if you'd like changes, or say 'approved' to complete the spec."
- Wait for explicit approval

### Completion

After tasks approved:
- Inform user the spec workflow is complete
- Summarize created files
- Suggest: "Use `/executing-kiro-tasks` to begin implementing tasks one at a time, or `/reviewing-kiro-specs` to review the spec."
- DO NOT begin implementing - that's a separate workflow

## Examples

**Input:** "Create a spec for dark mode toggle"

**Output sequence:**
1. Creates `.claude/specs/dark-mode-toggle/requirements.md` with EARS-formatted user stories
2. Presents summary: "I've created requirements for dark mode including theme persistence, system preference detection, and accessibility considerations."
3. Waits for approval
4. Creates `design.md` with component architecture
5. Waits for approval
6. Creates `tasks.md` with 8 implementation steps
7. Waits for approval
8. Reports completion

**Input:** "The requirements look good but add offline support"

**Output:** Updates requirements.md, presents new summary, asks for approval again

## Guidelines

1. **Generate first, ask later** - Don't ask 20 clarifying questions. Make reasonable assumptions and let the user correct.

2. **Explicit approval gates** - MUST wait for clear approval ("yes", "approved", "looks good", "lgtm") between each phase.

3. **One phase at a time** - Complete requirements before design, design before tasks.

4. **Summaries, not dumps** - Present summaries after writing, not full document contents.

5. **User controls pace** - Never auto-proceed to the next phase.

6. **Coding tasks only** - Implementation plan must NOT include:
   - User acceptance testing
   - Deployment to production
   - Performance metrics gathering
   - Documentation creation
   - Marketing activities

7. **Incremental complexity** - Each task builds on previous tasks with no orphaned code.

## References

- [ears-format.md](./references/ears-format.md) - EARS requirements syntax guide
