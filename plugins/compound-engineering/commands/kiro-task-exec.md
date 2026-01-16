---
name: kiro-task-exec
description: Execute tasks from a Kiro spec one at a time
argument-hint: "[spec folder path or 'next']"
---

# Kiro Task Exec

Execute implementation tasks from a spec, one at a time.

## Input

<spec_path> #$ARGUMENTS </spec_path>

If no path provided or just "next":
1. List available specs in `.claude/specs/`
2. Ask which spec to work on (or continue current one)

## Instructions

Follow the kiro-task-exec skill workflow exactly:

1. **Load context** - Read requirements.md, design.md, and tasks.md from the spec folder
2. **Find next task** - Locate first unchecked `- [ ]` item
3. **Confirm** - Ask user before starting: "The next task is [X]. Start?"
4. **Execute** - Implement the task following the design
5. **Update** - Mark task complete in tasks.md (`- [x]`)
6. **Stop** - Summarize what was done, wait for user

Key rules:
- ONE task at a time
- Always read spec files first for context
- Never auto-continue to next task
- Respect the spec - don't add unplanned features
