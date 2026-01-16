---
name: dspy-ruby
description: Build type-safe LLM applications with DSPy.rb
argument-hint: "[what to build or help with]"
---

# DSPy Ruby

Build type-safe, composable LLM applications using DSPy.rb.

## Input

<request> #$ARGUMENTS </request>

## Instructions

Follow the dspy-ruby skill to help with:

- **Signatures** - Define typed input/output contracts
- **Modules** - Build composable LLM components
- **Providers** - Configure OpenAI, Anthropic, Gemini, Ollama
- **Agents** - Create tool-using agents
- **Optimization** - Tune prompts automatically
- **Testing** - Test LLM-powered features

## Example Signature

```ruby
class Summarize < DSPy::Signature
  input :text, String, desc: "Text to summarize"
  output :summary, String, desc: "Concise summary"
end
```

## Example

```
/dspy-ruby create a sentiment analysis module
/dspy-ruby help me configure the Anthropic provider
```
