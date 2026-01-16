---
name: gemini-imagegen
description: Generate or edit images using Google's Gemini API
argument-hint: "[prompt or 'edit' for editing mode]"
---

# Gemini Image Generation

Generate and edit images using Google's Gemini API (Imagen 3).

## Input

<prompt> #$ARGUMENTS </prompt>

## Modes

### Generate (default)
Create a new image from a text prompt.

Use the Gemini MCP tools:
- `mcp__gemini__gemini-generate-image` for single images
- `mcp__gemini__gemini-start-image-edit` to start an editing session

### Edit
Start an interactive editing session:
1. Generate base image with `gemini-start-image-edit`
2. Refine with `gemini-continue-image-edit` using the session ID
3. End with `gemini-end-image-edit`

## Options

- **aspectRatio**: 1:1, 16:9, 9:16, 4:3, 3:4, etc.
- **imageSize**: 1K (fast), 2K (balanced), 4K (highest quality)
- **style**: photorealistic, watercolor, anime, oil painting, etc.

## Requirements

- `GEMINI_API_KEY` environment variable

## Examples

- `/gemini-imagegen a serene mountain lake at sunset`
- `/gemini-imagegen edit` (starts interactive session)
- `/gemini-imagegen cyberpunk cityscape --style neon --aspectRatio 16:9`
