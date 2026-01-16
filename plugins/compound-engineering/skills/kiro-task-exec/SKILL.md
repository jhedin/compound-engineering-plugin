---
name: kiro-task-exec
description: This skill executes implementation tasks from a Kiro spec one at a time with user review between each task. Use when the user wants to implement tasks from a spec, work through a task list, or continue implementation of a planned feature. Adapted from Amazon Kiro's task execution workflow.
---

# Kiro Task Exec

Execute implementation tasks from a spec, one at a time with user review.

## Quick Start

```
User: "/kiro-task-exec dark-mode-toggle"

1. Read requirements.md, design.md, tasks.md
2. Find first unchecked task
3. Ask: "The next task is X. Start?"
4. Implement task
5. Mark complete in tasks.md
6. Stop and wait for user
```

## Instructions

### Before Executing

ALWAYS read all spec files first:
- `.claude/specs/{feature}/requirements.md`
- `.claude/specs/{feature}/design.md`
- `.claude/specs/{feature}/tasks.md`

Executing tasks without this context leads to inaccurate implementations.

### Finding the Spec

If the user doesn't specify which spec:
1. List available specs: `ls .claude/specs/`
2. Ask which spec to work on
3. Wait for confirmation before proceeding

### Task Selection

**If user doesn't specify which task:**
1. Read tasks.md
2. Find first unchecked task (`- [ ]`)
3. Recommend it: "The next task is [task]. Would you like me to start?"
4. Wait for confirmation

**If user specifies a task:**
- "Start task 2" → Begin task 2
- "Do 1.3" → Begin sub-task 1.3
- "Next" → Find and start next unchecked task

### During Execution

1. **Reference requirements** - Check what requirement this task implements
2. **Follow the design** - Use architecture and patterns from design.md
3. **Write tests first** - If task is TDD-focused, tests before implementation
4. **Keep changes focused** - Only implement what this task requires
5. **No scope creep** - Don't fix unrelated issues or add unplanned features

### After Completion

1. **Update tasks.md** - Change `- [ ]` to `- [x]`
2. **Summarize what was done:**
   - Files created/modified
   - Tests added
   - Key implementation decisions
3. **Note deviations** - If you deviated from the plan, explain why
4. **STOP** - Wait for user review
5. **DO NOT auto-continue** - Let user decide when to proceed

## Examples

**Input:** "/kiro-task-exec auth-feature"

**Output:**
```
I've loaded the auth-feature spec:
- Requirements: 5 user stories with 23 acceptance criteria
- Design: JWT-based authentication with refresh tokens
- Tasks: 12 tasks, 3 completed, 9 remaining

The next task is:
- [ ] 4. Implement token refresh endpoint
  - Implements requirement 2.3
  - Create POST /auth/refresh endpoint

Would you like me to start on this task?
```

**Input:** "What's the next task?"

**Output:** Provides information without starting execution

**Input:** "Start task 4"

**Output:** Implements task 4, updates tasks.md, summarizes work, stops

## Guidelines

1. **ONE task at a time** - Never implement multiple tasks in one go.

2. **Always load context** - Read all three spec files before any task.

3. **Confirm before starting** - Ask user before beginning work.

4. **Stop after each task** - Present summary and wait for user.

5. **Respect the spec** - The spec represents agreed-upon requirements:
   - Do NOT change requirements without user approval
   - Do NOT deviate from design without explaining why
   - Do NOT add features not in the tasks
   - If spec needs updating, stop and discuss

6. **Distinguish questions from execution:**
   - "What's the next task?" → Information only
   - "How many tasks left?" → Information only
   - "Start task 2" → Begin execution
   - "Do the next task" → Begin execution
