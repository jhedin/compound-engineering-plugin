---
name: andrew-kane-gem
description: Write Ruby gems following Andrew Kane's patterns
argument-hint: "[gem name or description]"
---

# Andrew Kane Gem Writer

Write Ruby gems following Andrew Kane's proven patterns and philosophy.

## Input

<gem_info> #$ARGUMENTS </gem_info>

## Instructions

Follow the andrew-kane-gem-writer skill to create gems with:

- **Minimal dependencies** - Only what's absolutely necessary
- **Clean APIs** - Simple, intuitive method signatures
- **Excellent documentation** - README with clear examples
- **Sensible defaults** - Works out of the box
- **Production-ready** - Battle-tested patterns

## Structure

```
gem-name/
├── lib/
│   ├── gem_name.rb
│   └── gem_name/
│       └── version.rb
├── test/
├── Gemfile
├── gem_name.gemspec
├── LICENSE.txt
└── README.md
```

## Example

```
/andrew-kane-gem searchkick-lite "A lightweight search gem"
```
