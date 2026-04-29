# Portkey Configuration
_Last updated: 2026-04-22_

## API Setup

**Base URL:** `https://api.portkey.ai/v1`
**API Key env var:** `PORTKEY_API_KEY`

```bash
export PORTKEY_API_KEY="UgKiRSUEFAHGSTWBjOQNXDwkKKj/"  # old key — routes to Claude
export PORTKEY_API_KEY="VwFslTtBMP/j3m4i/HkmvyEv/mlR"   # new key — routes to real providers
export GEMINI_API_KEY="AIzaSyCuBfskGih3UchLQ4LrrX1622sRqbfVpQk"  # AI Studio direct — use for grounding
```

---

## Platform Virtual Keys

| Platform | Provider String | Model | Status | Notes |
|---|---|---|---|---|
| **ChatGPT (Azure OpenAI)** | `@azure-openai-bbfaac` | `gpt-5` | ✅ Active | Responses API + web_search_preview |
| **Perplexity** | `@perplexity-ai/sonar-pro` | `sonar-pro` | ⏸️ Parked — needs paid API ($5 min credit) | Free tier has no API access. Add when budget available. |
| **Gemini** | `@content-rnd-gem-565e6c` | `gemini-2.5-pro` | ⚠️ Portkey strips groundingMetadata | Use direct AI Studio key instead — see GEMINI_API_KEY below |
| **Claude** | `@vertex-global-region` | `claude-sonnet-4-5` | ✅ Active (no citations) | Tool_use only — no inline source URLs. Answer quality only. Also has `claude-opus-4-5` for higher quality. |

---

## Response Shapes — What Each Platform Returns

### ChatGPT (Responses API)
```json
{
  "output_text": "Formative assessment is...",
  "output": [{
    "type": "message",
    "content": [{
      "type": "output_text",
      "text": "...",
      "annotations": [{
        "type": "url_citation",
        "url_citation": {
          "url": "https://...",
          "title": "Page title",
          "start_index": 42,
          "end_index": 180
        }
      }]
    }]
  }]
}
```

### Perplexity (Chat Completions, strict-openai-compliance: false)
```json
{
  "choices": [{"message": {"content": "Formative assessment is..."}}],
  "citations": [
    "https://www.renaissance.com/edword/formative-assessment/",
    "https://www.formative.com/read/what-is-formative-assessment"
  ],
  "search_results": [
    {"url": "https://...", "title": "...", "date": "2025-01-01"}
  ]
}
```
`search_results[]` is richer than `citations[]` — use when available (Sonar Pro).

### Gemini (Chat Completions + google_search grounding)
```json
{
  "choices": [{"message": {"content": "Formative assessment is..."}}],
  "groundingMetadata": {
    "webSearchQueries": ["what is formative assessment"],
    "groundingChunks": [
      {"web": {"uri": "https://...", "title": "Page title"}}
    ],
    "groundingSupports": [
      {
        "segment": {"startIndex": 0, "endIndex": 120, "text": "..."},
        "groundingChunkIndices": [0, 1]
      }
    ]
  }
}
```
Note: Portkey SDK may strip `groundingMetadata`. Set `strict-openai-compliance: false` header. If still absent, use raw HTTP fallback.

### Claude (Chat Completions + tool_use)
```json
{
  "choices": [{
    "message": {
      "content": "...",
      "tool_calls": [{
        "function": {
          "name": "web_search",
          "arguments": "{\"query\": \"what is formative assessment\"}"
        }
      }]
    }
  }]
}
```
Claude requires a second turn with tool results to get actual content + URLs. Not ideal for citation extraction in single-turn flow.

---

## Platform Code Patterns

```python
from portkey_ai import Portkey

# ── ChatGPT ────────────────────────────────────────────────────────────────
portkey = Portkey(api_key="PORTKEY_API_KEY", provider="@azure-openai-bbfaac")
response = portkey.responses.create(
    model="gpt-5",
    tools=[{"type": "web_search_preview", "search_context_size": "high"}],
    input="what is formative assessment?",
)
# Sources: response.output[].content[].annotations[type=url_citation].url_citation.url

# ── Perplexity ─────────────────────────────────────────────────────────────
portkey = Portkey(
    api_key="PORTKEY_API_KEY",
    provider="@perplexity-ai/sonar-pro",
    customHeaders={"strict-openai-compliance": "false"},
)
response = portkey.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "what is formative assessment?"}],
)
# Sources: response.citations[] or response.search_results[]

# ── Gemini ─────────────────────────────────────────────────────────────────
portkey = Portkey(
    apiKey="PORTKEY_API_KEY",
    provider="@content-rnd-gem-565e6c",   # confirmed virtual key
    customHeaders={"strict-openai-compliance": "false"},
)
response = portkey.chat.completions.create(
    model="gemini-2.0-flash-001",
    messages=[{"role": "user", "content": "what is formative assessment?"}],
    tools=[{"type": "function", "function": {"name": "google_search"}}],
)
# Sources: response.groundingMetadata.groundingChunks[].web.uri

# ── Claude ─────────────────────────────────────────────────────────────────
portkey = Portkey(api_key="PORTKEY_API_KEY", provider="@aws-us-east-1")
response = portkey.chat.completions.create(
    model="anthropic.claude-3-5-sonnet-20241022-v2:0",
    messages=[{"role": "user", "content": "what is formative assessment?"}],
)
# No citations — answer quality only
```

---

## Install & Test

```bash
cd ~/.openclaw/workspace/skills/geo-query
npm init -y
npm install portkey-ai

export PORTKEY_API_KEY="UgKiRSUEFAHGSTWBjOQNXDwkKKj/"

# Single platform test
node scripts/geo-query.js --query "what is formative assessment?" --platforms chatgpt

# All platforms
node scripts/geo-query.js --query "what is formative assessment?" --platforms all

# Full calibration batch
node scripts/geo-query.js \
  --batch references/calibration-queries.json \
  --platforms chatgpt,perplexity \
  --output ../../../memory/research/geo-runs/2026-04-22-calibration.json
```
