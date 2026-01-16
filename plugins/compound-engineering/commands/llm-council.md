---
name: llm-council
description: Query multiple AI models and synthesize the best answer
argument-hint: "[your question]"
---

# LLM Council

Run a multi-model deliberative ensemble inspired by Andrej Karpathy's llm-council.

## Input

<question> #$ARGUMENTS </question>

If no question provided, ask the user what they want the council to deliberate on.

## Instructions

Run the council script:

```bash
cd ~/.claude/plugins/marketplaces/every-marketplace/plugins/compound-engineering/skills/llm-council/scripts
python council.py --show-individual "USER_QUESTION_HERE"
```

If OPENROUTER_API_KEY is not set, guide the user:
1. Sign up at https://openrouter.ai (free tier available)
2. Get API key from https://openrouter.ai/keys
3. Export: `export OPENROUTER_API_KEY='sk-or-...'`

## Process

The council runs three stages:
1. **First Opinions** - All models answer in parallel
2. **Peer Review** - Each model reviews others' responses (anonymized)
3. **Chairman Synthesis** - Final answer combining best insights

Present the synthesized final answer prominently, with individual responses in collapsible sections if requested.
