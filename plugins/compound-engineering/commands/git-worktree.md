---
name: git-worktree
description: Manage Git worktrees for parallel development
argument-hint: "[list|create|switch|clean]"
---

# Git Worktree

Manage Git worktrees for isolated parallel development.

## Input

<action> #$ARGUMENTS </action>

## Actions

### list (default)
Show all existing worktrees:
```bash
git worktree list
```

### create [branch-name]
Create a new worktree for a branch:
```bash
git worktree add ../repo-branch-name branch-name
```

### switch [worktree-path]
Guide the user to cd to the worktree path. Note: Claude cannot change the user's working directory.

### clean
Remove worktrees for merged/deleted branches:
```bash
git worktree prune
```

## Usage Examples

- `/git-worktree list` - Show all worktrees
- `/git-worktree create feature-auth` - Create worktree for feature-auth branch
- `/git-worktree clean` - Prune stale worktrees
