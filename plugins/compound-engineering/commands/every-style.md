---
name: every-style
description: Review and edit copy for Every's style guide compliance
argument-hint: "[file path or text to review]"
---

# Every Style Editor

Review and edit content to conform to Every's specific style guide.

## Input

<content> #$ARGUMENTS </content>

## Instructions

Follow the every-style-editor skill to check for:

- **Title case** in headlines
- **Sentence case** elsewhere
- **Company singular/plural** usage
- **Overused words** to avoid
- **Passive voice** detection
- **Number formatting** rules
- **Punctuation** conventions

## Review Process

1. Read the content thoroughly
2. Check each style rule systematically
3. Provide specific line-by-line feedback
4. Suggest corrections with explanations

## Example

```
/every-style docs/blog-post.md
/every-style "Check this headline: The Future Of AI Is Here"
```
