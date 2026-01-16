#!/usr/bin/env python3
"""
LLM Council - Multi-model deliberative ensemble
Inspired by Andrej Karpathy's llm-council

Queries multiple LLMs, has them review each other's work (anonymized),
then a chairman synthesizes the final answer.
"""

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Optional
import httpx

# Configuration
CONFIG_PATH = Path(__file__).parent / "council_config.json"

DEFAULT_CONFIG = {
    "models": [
        "deepseek/deepseek-r1:free",
        "google/gemini-2.0-flash-001",
        "anthropic/claude-3.5-sonnet",
        "openai/gpt-4o"
    ],
    "chairman": "anthropic/claude-3.5-sonnet",
    "timeout": 120,
    "max_tokens": 4096
}

def load_config() -> dict:
    """Load configuration from file or use defaults."""
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH) as f:
            user_config = json.load(f)
            return {**DEFAULT_CONFIG, **user_config}
    return DEFAULT_CONFIG

def get_api_key() -> str:
    """Get OpenRouter API key from environment."""
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        print("ERROR: OPENROUTER_API_KEY environment variable not set", file=sys.stderr)
        print("\nTo set up:", file=sys.stderr)
        print("1. Sign up at https://openrouter.ai", file=sys.stderr)
        print("2. Get your API key from https://openrouter.ai/keys", file=sys.stderr)
        print("3. Export it: export OPENROUTER_API_KEY='sk-or-...'", file=sys.stderr)
        sys.exit(1)
    return key

async def query_model(
    client: httpx.AsyncClient,
    model: str,
    messages: list[dict],
    api_key: str,
    config: dict
) -> dict:
    """Query a single model via OpenRouter."""
    try:
        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/llm-council-plugin",
                "X-Title": "LLM Council Plugin"
            },
            json={
                "model": model,
                "messages": messages,
                "max_tokens": config.get("max_tokens", 4096),
            },
            timeout=config.get("timeout", 120)
        )
        response.raise_for_status()
        data = response.json()
        content = data["choices"][0]["message"]["content"]
        return {"model": model, "response": content, "error": None}
    except httpx.TimeoutException:
        return {"model": model, "response": None, "error": "Timeout"}
    except httpx.HTTPStatusError as e:
        return {"model": model, "response": None, "error": f"HTTP {e.response.status_code}"}
    except Exception as e:
        return {"model": model, "response": None, "error": str(e)}

async def stage1_first_opinions(
    client: httpx.AsyncClient,
    query: str,
    models: list[str],
    api_key: str,
    config: dict
) -> list[dict]:
    """Stage 1: Get initial responses from all models in parallel."""
    print("\n## Stage 1: Gathering First Opinions\n", file=sys.stderr)

    messages = [{"role": "user", "content": query}]

    tasks = [
        query_model(client, model, messages, api_key, config)
        for model in models
    ]

    results = await asyncio.gather(*tasks)

    for result in results:
        model_name = result["model"].split("/")[-1]
        if result["error"]:
            print(f"  - {model_name}: ERROR - {result['error']}", file=sys.stderr)
        else:
            print(f"  - {model_name}: OK ({len(result['response'])} chars)", file=sys.stderr)

    return results

async def stage2_peer_review(
    client: httpx.AsyncClient,
    query: str,
    stage1_results: list[dict],
    api_key: str,
    config: dict
) -> list[dict]:
    """Stage 2: Each model reviews others' responses (anonymized)."""
    print("\n## Stage 2: Peer Review\n", file=sys.stderr)

    # Filter successful responses
    valid_results = [r for r in stage1_results if r["response"]]

    if len(valid_results) < 2:
        print("  Not enough valid responses for peer review", file=sys.stderr)
        return []

    reviews = []

    for i, reviewer in enumerate(valid_results):
        # Build anonymized view of other responses
        others = []
        for j, other in enumerate(valid_results):
            if i != j:
                letter = chr(65 + len(others))  # A, B, C, ...
                others.append(f"### Response {letter}\n{other['response']}")

        review_prompt = f"""Original question: {query}

Here are responses from different AI assistants (anonymized):

{chr(10).join(others)}

---

Please review these responses. For each one:
1. Rate it 1-10 for accuracy and insight
2. Note any errors or missing information
3. Identify the strongest response overall

Be concise but thorough. Format as:
**Response A**: [score]/10 - [brief assessment]
**Response B**: [score]/10 - [brief assessment]
...
**Best Overall**: [letter] because [reason]"""

        messages = [{"role": "user", "content": review_prompt}]
        result = await query_model(client, reviewer["model"], messages, api_key, config)
        result["reviewing"] = reviewer["model"]
        reviews.append(result)

        model_name = reviewer["model"].split("/")[-1]
        if result["error"]:
            print(f"  - {model_name}'s review: ERROR", file=sys.stderr)
        else:
            print(f"  - {model_name}'s review: OK", file=sys.stderr)

    return reviews

async def stage3_chairman_synthesis(
    client: httpx.AsyncClient,
    query: str,
    stage1_results: list[dict],
    stage2_reviews: list[dict],
    chairman_model: str,
    api_key: str,
    config: dict
) -> str:
    """Stage 3: Chairman synthesizes all responses and reviews into final answer."""
    print("\n## Stage 3: Chairman Synthesis\n", file=sys.stderr)

    # Build the synthesis prompt
    responses_text = []
    for i, result in enumerate(stage1_results):
        if result["response"]:
            model_name = result["model"].split("/")[-1]
            responses_text.append(f"### {model_name}\n{result['response']}")

    reviews_text = []
    for review in stage2_reviews:
        if review["response"]:
            reviewer = review["reviewing"].split("/")[-1]
            reviews_text.append(f"### {reviewer}'s Review\n{review['response']}")

    synthesis_prompt = f"""You are the Chairman of an LLM Council. Your role is to synthesize multiple AI responses into one excellent final answer.

## Original Question
{query}

## Individual Responses
{chr(10).join(responses_text)}

## Peer Reviews
{chr(10).join(reviews_text)}

---

Based on the responses and peer reviews above, provide the definitive answer to the original question.

Guidelines:
- Incorporate the best insights from all responses
- Correct any errors identified in the reviews
- Be comprehensive but concise
- If there's genuine disagreement, acknowledge it
- Cite which model(s) contributed key insights when relevant

Provide your synthesized final answer:"""

    messages = [{"role": "user", "content": synthesis_prompt}]
    result = await query_model(client, chairman_model, messages, api_key, config)

    chairman_name = chairman_model.split("/")[-1]
    if result["error"]:
        print(f"  - Chairman ({chairman_name}): ERROR - {result['error']}", file=sys.stderr)
        return f"Chairman synthesis failed: {result['error']}"
    else:
        print(f"  - Chairman ({chairman_name}): OK", file=sys.stderr)
        return result["response"]

async def run_council(query: str) -> dict:
    """Run the full council deliberation process."""
    config = load_config()
    api_key = get_api_key()

    models = config["models"]
    chairman = config["chairman"]

    print(f"\n{'='*60}", file=sys.stderr)
    print("LLM COUNCIL DELIBERATION", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)
    print(f"\nCouncil Members: {', '.join(m.split('/')[-1] for m in models)}", file=sys.stderr)
    print(f"Chairman: {chairman.split('/')[-1]}", file=sys.stderr)
    print(f"\nQuery: {query[:100]}{'...' if len(query) > 100 else ''}", file=sys.stderr)

    async with httpx.AsyncClient() as client:
        # Stage 1: First opinions
        stage1 = await stage1_first_opinions(client, query, models, api_key, config)

        # Stage 2: Peer review
        stage2 = await stage2_peer_review(client, query, stage1, api_key, config)

        # Stage 3: Chairman synthesis
        final = await stage3_chairman_synthesis(
            client, query, stage1, stage2, chairman, api_key, config
        )

    print(f"\n{'='*60}\n", file=sys.stderr)

    return {
        "query": query,
        "stage1_responses": stage1,
        "stage2_reviews": stage2,
        "final_answer": final,
        "config": {
            "models": models,
            "chairman": chairman
        }
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: council.py <query>", file=sys.stderr)
        print("       council.py --show-individual <query>", file=sys.stderr)
        sys.exit(1)

    show_individual = False
    query_start = 1

    if sys.argv[1] == "--show-individual":
        show_individual = True
        query_start = 2

    if query_start >= len(sys.argv):
        print("ERROR: No query provided", file=sys.stderr)
        sys.exit(1)

    query = " ".join(sys.argv[query_start:])

    result = asyncio.run(run_council(query))

    # Output
    if show_individual:
        print("# Individual Responses\n")
        for resp in result["stage1_responses"]:
            if resp["response"]:
                model = resp["model"].split("/")[-1]
                print(f"## {model}\n")
                print(resp["response"])
                print("\n---\n")

        print("# Peer Reviews\n")
        for review in result["stage2_reviews"]:
            if review["response"]:
                reviewer = review["reviewing"].split("/")[-1]
                print(f"## {reviewer}'s Review\n")
                print(review["response"])
                print("\n---\n")

        print("# Final Answer (Chairman)\n")

    print(result["final_answer"])

if __name__ == "__main__":
    main()
