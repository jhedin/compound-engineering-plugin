---
name: llm-council
description: This skill implements a multi-model deliberative ensemble inspired by Andrej Karpathy's LLM Council. Use when the user wants multiple AI models to collaborate on answering a question, needs diverse perspectives on a problem, or wants higher-quality answers through peer review and synthesis.
---

# LLM Council

Multi-model deliberative ensemble inspired by [Andrej Karpathy's llm-council](https://github.com/karpathy/llm-council).

## Overview

The LLM Council queries multiple AI models via OpenRouter, has them anonymously review each other's responses, then synthesizes the best answer through a "chairman" model.

**Three-stage process:**
1. **First Opinions** - All council members answer the question in parallel
2. **Peer Review** - Each model reviews others' responses (anonymized as Response A, B, C...)
3. **Chairman Synthesis** - A designated model synthesizes all responses and reviews into a final answer

## Requirements

- `OPENROUTER_API_KEY` environment variable ([get one free at openrouter.ai](https://openrouter.ai))
- Python 3.10+ with `httpx` package

## Usage

Run the council script with the user's question:

```bash
cd ~/.claude/plugins/marketplaces/every-marketplace/plugins/compound-engineering/skills/llm-council/scripts
python council.py "What is the best approach to implement authentication in a Rails API?"
```

For detailed output including individual responses and reviews:

```bash
python council.py --show-individual "Your question here"
```

## Configuration

Create `council_config.json` in the scripts directory to customize:

```json
{
  "models": [
    "deepseek/deepseek-r1-0528:free",
    "google/gemini-2.0-flash-exp:free",
    "meta-llama/llama-3.3-70b-instruct:free",
    "mistralai/mistral-small-3.1-24b-instruct:free"
  ],
  "chairman": "deepseek/deepseek-r1-0528:free",
  "timeout": 120,
  "max_tokens": 4096
}
```

### Available Models

**Free models** (no cost, rate-limited):
- `deepseek/deepseek-r1-0528:free` - DeepSeek R1 (reasoning model)
- `google/gemini-2.0-flash-exp:free` - Gemini 2.0 Flash
- `google/gemma-3-27b-it:free` - Gemma 3 27B
- `meta-llama/llama-3.3-70b-instruct:free` - Llama 3.3 70B
- `mistralai/mistral-small-3.1-24b-instruct:free` - Mistral Small

**Paid flagship models** (add credits to use):
- `openai/gpt-4o` - GPT-4o
- `anthropic/claude-3.5-sonnet` - Claude 3.5 Sonnet
- `google/gemini-2.0-flash-001` - Gemini 2.0 Flash (paid tier)
- `x-ai/grok-2` - Grok 2

## When to Use

- Complex questions that benefit from multiple perspectives
- Technical decisions where different models may have different strengths
- When you want higher confidence in an answer through consensus
- Research questions where diverse viewpoints add value

## Installation

If the skill hasn't been set up yet:

```bash
cd ~/.claude/plugins/marketplaces/every-marketplace/plugins/compound-engineering/skills/llm-council/scripts
pip install -r requirements.txt
```

Set your OpenRouter API key:

```bash
export OPENROUTER_API_KEY='sk-or-v1-...'
```

## Example Output

```
============================================================
LLM COUNCIL DELIBERATION
============================================================

Council Members: deepseek-r1-0528, gemini-2.0-flash-exp, llama-3.3-70b-instruct
Chairman: deepseek-r1-0528

Query: What is the best database for a real-time chat application?

## Stage 1: Gathering First Opinions

  - deepseek-r1-0528: OK (2341 chars)
  - gemini-2.0-flash-exp: OK (1892 chars)
  - llama-3.3-70b-instruct: OK (2156 chars)

## Stage 2: Peer Review

  - deepseek-r1-0528's review: OK
  - gemini-2.0-flash-exp's review: OK
  - llama-3.3-70b-instruct's review: OK

## Stage 3: Chairman Synthesis

  - Chairman (deepseek-r1-0528): OK

============================================================

[Final synthesized answer appears here]
```

## See Also

- [scripts/council.py](./scripts/council.py) - Main council implementation
- [scripts/requirements.txt](./scripts/requirements.txt) - Python dependencies
