---
name: consulting-llm-council
description: This skill queries multiple AI models via OpenRouter, has them peer-review each other's responses, then synthesizes the best answer. Use when the user wants diverse AI perspectives, needs consensus on complex questions, or wants higher-quality answers through deliberation. Inspired by Andrej Karpathy's LLM Council.
---

# LLM Council

Query multiple AI models, have them peer-review each other, and synthesize the best answer.

## Quick Start

```bash
cd ~/.claude/plugins/marketplaces/every-marketplace/plugins/compound-engineering/skills/consulting-llm-council/scripts
python council.py "What's the best database for real-time chat?"
```

Requires: `OPENROUTER_API_KEY` environment variable

## Instructions

### Running the Council

Execute [council.py](./scripts/council.py) with the user's question:

```bash
python council.py "Your question here"
```

For detailed output including individual responses and peer reviews:

```bash
python council.py --show-individual "Your question here"
```

### Three-Stage Process

1. **First Opinions** - All council members answer the question in parallel
2. **Peer Review** - Each model reviews others' responses (anonymized as Response A, B, C...)
3. **Chairman Synthesis** - A designated model synthesizes all responses and reviews into a final answer

### Handling Missing API Key

If `OPENROUTER_API_KEY` is not set, guide the user:
1. Sign up at https://openrouter.ai (free tier available)
2. Get API key from https://openrouter.ai/keys
3. Export: `export OPENROUTER_API_KEY='sk-or-v1-...'`

### Configuration

Create `council_config.json` in the scripts directory to customize models:

```json
{
  "models": [
    "deepseek/deepseek-r1-0528:free",
    "google/gemini-2.0-flash-exp:free",
    "meta-llama/llama-3.3-70b-instruct:free"
  ],
  "chairman": "deepseek/deepseek-r1-0528:free",
  "timeout": 120,
  "max_tokens": 4096
}
```

## Examples

**Input:** "What's the best approach to implement authentication in a Rails API?"

**Output:**
```
============================================================
LLM COUNCIL DELIBERATION
============================================================

Council Members: deepseek-r1-0528, gemini-2.0-flash-exp, llama-3.3-70b-instruct
Chairman: deepseek-r1-0528

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

[Final synthesized answer incorporating best insights from all models]
```

**Presenting results:** Show the final synthesized answer prominently. Optionally include individual responses in collapsible sections.

## Guidelines

1. **When to use:**
   - Complex questions benefiting from multiple perspectives
   - Technical decisions where different models have different strengths
   - When higher confidence through consensus is desired
   - Research questions where diverse viewpoints add value

2. **Available models:**

   **Free (rate-limited):**
   - `deepseek/deepseek-r1-0528:free` - Reasoning model
   - `google/gemini-2.0-flash-exp:free` - Fast multimodal
   - `meta-llama/llama-3.3-70b-instruct:free` - Open source
   - `mistralai/mistral-small-3.1-24b-instruct:free` - European AI

   **Paid flagships:**
   - `openai/gpt-4o` - GPT-4o
   - `anthropic/claude-3.5-sonnet` - Claude
   - `x-ai/grok-2` - Grok

3. **Installation:** If dependencies are missing:
   ```bash
   pip install -r scripts/requirements.txt
   ```

## References

- [scripts/council.py](./scripts/council.py) - Main council implementation
- [scripts/requirements.txt](./scripts/requirements.txt) - Python dependencies
- [Karpathy's llm-council](https://github.com/karpathy/llm-council) - Original inspiration
