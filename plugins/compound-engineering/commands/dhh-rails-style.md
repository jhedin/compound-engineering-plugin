---
name: dhh-rails-style
description: Write Ruby/Rails code in DHH's 37signals style
argument-hint: "[file or description of what to write]"
---

# DHH Rails Style

Write Ruby and Rails code following David Heinemeier Hansson's 37signals conventions.

## Input

<target> #$ARGUMENTS </target>

## Instructions

Follow the dhh-rails-style skill when writing or reviewing Ruby/Rails code.

Key principles:
- **REST purity** - Resources over custom actions
- **Fat models, thin controllers** - Business logic in models
- **Current attributes** - Use `Current.user` pattern
- **Hotwire-first** - Turbo + Stimulus, minimal JavaScript
- **Clarity over cleverness** - Simple, readable code
- **Convention over configuration** - Follow Rails defaults

## When to Apply

- Writing new Rails controllers, models, or views
- Refactoring existing Rails code
- Code review of Rails PRs
- Architectural decisions in Rails apps

## Example

```
/dhh-rails-style app/controllers/posts_controller.rb
```

Will review and suggest changes to match DHH's style.
