---
name: kiro-task-exec
description: This skill executes tasks from an existing spec one at a time. Use when the user wants to implement tasks from a spec, work through a task list, or continue implementation of a planned feature. Adapted from Amazon Kiro's task execution workflow.
---

# Kiro Task Execution

Execute implementation tasks from a spec, one at a time.

## Prerequisites

Before executing any tasks, ALWAYS read these files first:
- `.claude/specs/{feature}/requirements.md`
- `.claude/specs/{feature}/design.md`
- `.claude/specs/{feature}/tasks.md`

Executing tasks without this context leads to inaccurate implementations that don't match the spec.

## Finding the Spec

If the user doesn't specify which spec:
1. List available specs: `ls .claude/specs/`
2. Ask user which spec to work on
3. Wait for confirmation before proceeding

## Execution Rules

**CRITICAL: ONE TASK AT A TIME**

1. Only work on ONE task at a time
2. Look at task details in the task list
3. If a task has sub-tasks (1.1, 1.2), complete sub-tasks first
4. Verify implementation against the referenced requirements
5. After completing a task, STOP and let user review
6. DO NOT proceed to the next task without user explicitly asking

## Task Selection

If user doesn't specify which task:
1. Read the tasks.md file
2. Find the first unchecked task (`- [ ]`)
3. Recommend it: "The next task is [task]. Would you like me to start on it?"
4. Wait for confirmation before starting

If user specifies a task:
- "Start task 2" -> Begin task 2
- "Do 1.3" -> Begin sub-task 1.3
- "Next" -> Find and start the next unchecked task

## Answering Task Questions

Users may ask about tasks without wanting to execute them. Recognize the difference:

**Information requests (don't start executing):**
- "What's the next task?"
- "How many tasks are left?"
- "What does task 3 involve?"
- "Show me the task list"

**Execution requests (start working):**
- "Start task 2"
- "Do the next task"
- "Begin implementation"
- "Let's work on task 1.1"

## During Task Execution

1. **Reference the requirements** - Check what requirement this task implements
2. **Follow the design** - Use the architecture and patterns from design.md
3. **Write tests first** - If the task is TDD-focused, write tests before implementation
4. **Keep changes focused** - Only implement what this task requires
5. **No scope creep** - Don't fix unrelated issues or add features not in the task

## After Task Completion

1. **Update tasks.md** - Mark the task as complete by changing `- [ ]` to `- [x]`
2. **Summarize what was done:**
   - Files created/modified
   - Tests added
   - Key implementation decisions
3. **Note any deviations** - If you had to deviate from the plan, explain why
4. **STOP** - Wait for user to review
5. **DO NOT automatically continue** - Let user decide when to proceed

## Example Flow

User invokes the skill with a spec name. The assistant:

1. Reads all three spec files (requirements, design, tasks)
2. Identifies the next unchecked task
3. Asks for confirmation to start
4. Implements the task
5. Updates tasks.md to mark it complete
6. Summarizes what was done
7. Stops and waits for user

The user then reviews and either:
- Says "next" to continue to the next task
- Asks for changes to what was implemented
- Ends the session

## Important: Respect the Spec

The spec documents represent agreed-upon requirements and design. During task execution:

- Do NOT change requirements without user approval
- Do NOT deviate from the design architecture without explaining why
- Do NOT add features not in the tasks
- If you discover the spec needs updating, stop and discuss with the user
