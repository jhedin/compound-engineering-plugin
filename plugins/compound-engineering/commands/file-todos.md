---
name: file-todos
description: Manage file-based todo tracking in todos/ directory
argument-hint: "[list|add|complete|triage]"
---

# File Todos

Manage the file-based todo tracking system in the `todos/` directory.

## Input

<action> #$ARGUMENTS </action>

## Actions

### list (default)
Show all todos organized by status:
```bash
ls todos/*.md
```

### add [title]
Create a new todo file:
```
todos/YYYY-MM-DD-title.md
```

### complete [todo-file]
Mark a todo as complete by moving or updating its status.

### triage
Review and prioritize pending todos.

## Todo File Format

```markdown
---
status: pending|in_progress|completed
priority: p1|p2|p3
created: 2024-01-15
---

# Todo Title

Description and context...

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
```

## Example

```
/file-todos list
/file-todos add "Fix authentication bug"
/file-todos triage
```
