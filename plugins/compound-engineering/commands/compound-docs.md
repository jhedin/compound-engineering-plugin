---
name: compound-docs
description: Capture solved problems as categorized documentation
argument-hint: "[problem or solution to document]"
---

# Compound Docs

Capture solved problems as categorized documentation with YAML frontmatter for fast lookup.

## Input

<problem> #$ARGUMENTS </problem>

## Instructions

Follow the compound-docs skill to document:

1. **Problem** - What was the issue?
2. **Context** - When does this occur?
3. **Solution** - How was it solved?
4. **Category** - Tag for organization

## Output Location

`docs/solutions/{category}/{problem-slug}.md`

## Document Format

```markdown
---
title: Problem Title
category: debugging|architecture|performance|etc
tags: [tag1, tag2]
created: 2024-01-15
---

# Problem Title

## Problem

Description of the issue...

## Solution

How it was resolved...

## References

- Related links
```

## Example

```
/compound-docs "Fixed N+1 query in user dashboard"
/compound-docs document the authentication refactoring
```
