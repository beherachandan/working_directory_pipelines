/**
 * geo-query-test.mjs
 * Query any GEO engine (chatgpt | perplexity | gemini) via Portkey.
 * Returns answer text + extracted citations.
 *
 * Usage:
 *   node geo-query-test.mjs [options]
 *
 * Options:
 *   --query    "your query here"          (default: "What is formative assessment in education?")
 *   --platform chatgpt|perplexity|gemini  (default: chatgpt)
 *   --model    override model name        (optional)
 *
 * Examples:
 *   node geo-query-test.mjs --query "best tools for teachers" --platform chatgpt
 *   node geo-query-test.mjs --query "best tools for teachers" --platform perplexity
 *   node geo-query-test.mjs --query "best tools for teachers" --platform gemini
 *   node geo-query-test.mjs --query "best tools for teachers" --platform gemini --model gemini-2.5-pro
 *
 * Env vars (optional — hardcoded fallbacks below):
 *   PORTKEY_API_KEY   — key that routes to real GPT/Gemini/Perplexity (VwFsl...)
 *   PERPLEXITY_VIRTUAL_KEY — your Perplexity virtual key slug from Portkey dashboard
 */

import { Portkey } from 'portkey-ai';
import https from 'https';

// ── Keys ─────────────────────────────────────────────────────────────────────
// VwFsl... = "new" key that routes to real providers (not Claude fallback)
const PORTKEY_API_KEY = process.env.PORTKEY_API_KEY || 'VwFslTtBMP/j3m4i/HkmvyEv/mlR';

// Perplexity virtual key: set this after creating it in Portkey dashboard
// app.portkey.ai → Virtual Keys → Add New → Perplexity AI → paste Perplexity API key
const PERPLEXITY_VIRTUAL_KEY = process.env.PERPLEXITY_VIRTUAL_KEY || null;

// Gemini direct API key (AI Studio) — bypasses Portkey, gets real groundingMetadata
const GEMINI_API_KEY = process.env.GEMINI_API_KEY || 'AIzaSyCuBfskGih3UchLQ4LrrX1622sRqbfVpQk';

// ── Platform defaults ─────────────────────────────────────────────────────────
const PLATFORM_DEFAULTS = {
  chatgpt: {
    provider: '@azure-openai-bbfaac',
    model: 'gpt-5-mini',
    api: 'responses',
  },
  perplexity: {
    // Uses virtualKey (not provider) — Portkey Perplexity integration pattern
    model: 'sonar-pro',   // sonar-pro gives richer search_results[]; sonar = lightweight
    api: 'chat',
  },
  gemini: {
    provider: '@content-rnd-gem-565e6c',
    model: 'gemini-2.0-flash-001',
    api: 'chat',
  },
};

// ── CLI args ──────────────────────────────────────────────────────────────────
function parseArgs(argv) {
  const args = { query: null, platform: 'chatgpt', model: null };
  for (let i = 2; i < argv.length; i++) {
    if (argv[i] === '--query'    && argv[i + 1]) { args.query    = argv[++i]; continue; }
    if (argv[i] === '--platform' && argv[i + 1]) { args.platform = argv[++i]; continue; }
    if (argv[i] === '--model'    && argv[i + 1]) { args.model    = argv[++i]; continue; }
    if (!argv[i].startsWith('--') && !args.query)  { args.query  = argv[i]; }
  }
  args.query    = args.query    || 'What is formative assessment in education?';
  args.platform = args.platform.toLowerCase();
  return args;
}

// ── Citation extractors ───────────────────────────────────────────────────────
function extractChatGPTCitations(response) {
  const sources = [];
  for (const block of (response.output || [])) {
    for (const item of (block.content || [])) {
      for (const ann of (item.annotations || [])) {
        if (ann.type === 'url_citation') {
          const url   = ann.url   || ann.url_citation?.url;
          const title = ann.title || ann.url_citation?.title || '';
          if (url && !sources.find(s => s.url === url)) sources.push({ url, title });
        }
      }
    }
  }
  return sources;
}

function extractPerplexityCitations(response) {
  const sources = [];
  // search_results[] is richer (has titles); citations[] is URL-only fallback
  if (response.search_results?.length) {
    for (const r of response.search_results) {
      if (r.url && !sources.find(s => s.url === r.url))
        sources.push({ url: r.url, title: r.title || '' });
    }
  } else if (response.citations?.length) {
    for (const url of response.citations) {
      if (!sources.find(s => s.url === url)) sources.push({ url, title: '' });
    }
  }
  return sources;
}

function extractGeminiCitations(gm) {
  const sources = [];
  if (!gm) return sources;
  for (const chunk of (gm.groundingChunks || [])) {
    const web = chunk.web || chunk.retrievedContext;
    if (!web) continue;
    const url = web.uri || web.url || '';
    if (url && !sources.find(s => s.url === url))
      sources.push({ url, title: web.title || '' });
  }
  return sources;
}

// ── Raw HTTP helper (for Gemini — Portkey SDK strips groundingMetadata) ────────
function rawHttpPost(hostname, path, headers, body) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify(body);
    const req = https.request(
      { hostname, path, method: 'POST', headers: { ...headers, 'Content-Length': Buffer.byteLength(data) } },
      (res) => {
        let buf = '';
        res.on('data', d => buf += d);
        res.on('end', () => {
          try { resolve({ status: res.statusCode, body: JSON.parse(buf) }); }
          catch { resolve({ status: res.statusCode, body: buf }); }
        });
      }
    );
    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

// ── Platform runners ──────────────────────────────────────────────────────────

async function runChatGPT(query, model) {
  const portkey = new Portkey({ apiKey: PORTKEY_API_KEY, provider: PLATFORM_DEFAULTS.chatgpt.provider });
  const response = await portkey.responses.create({
    model,
    tools: [{ type: 'web_search_preview' }],
    input: query,
  });
  return { answer: response.output_text || '', sources: extractChatGPTCitations(response), raw: response };
}

async function runPerplexity(query, model) {
  if (!PERPLEXITY_VIRTUAL_KEY) {
    throw new Error(
      'PERPLEXITY_VIRTUAL_KEY not set.\n' +
      '  1. Go to app.portkey.ai → Virtual Keys → Add New\n' +
      '  2. Provider: Perplexity AI, paste your Perplexity API key\n' +
      '  3. Copy the slug and run:\n' +
      '     PERPLEXITY_VIRTUAL_KEY=<slug> node geo-query-test.mjs --platform perplexity ...'
    );
  }
  const portkey = new Portkey({
    apiKey: PORTKEY_API_KEY,
    virtualKey: PERPLEXITY_VIRTUAL_KEY,
    customHeaders: { 'strict-openai-compliance': 'false' },
  });
  const response = await portkey.chat.completions.create({
    model,
    messages: [{ role: 'user', content: query }],
  });
  const answer  = response.choices?.[0]?.message?.content || '';
  const sources = extractPerplexityCitations(response);
  return { answer, sources, raw: response };
}

async function runGemini(query, model) {
  // ── Attempt 1: Direct Gemini API (AI Studio key) — full groundingMetadata ──
  if (GEMINI_API_KEY) {
    console.log('[gemini] Using direct AI Studio API key...');
    // Map OpenAI-style model names to Gemini native names
    const geminiModel = model.startsWith('gemini-') ? model : 'gemini-2.0-flash';
    const result = await rawHttpPost(
      'generativelanguage.googleapis.com',
      `/v1beta/models/${geminiModel}:generateContent?key=${GEMINI_API_KEY}`,
      { 'Content-Type': 'application/json' },
      {
        contents: [{ parts: [{ text: query }] }],
        tools: [{ google_search: {} }],
      }
    );

    if (result.status === 429) {
      // Try fallback model first (separate quota), then wait + retry original
      const fallbackModel = geminiModel === 'gemini-2.0-flash' ? 'gemini-2.0-flash-lite' : null;
      if (fallbackModel) {
        console.log(`[gemini] Rate limited — trying fallback model ${fallbackModel}...`);
        const fallback = await rawHttpPost(
          'generativelanguage.googleapis.com',
          `/v1beta/models/${fallbackModel}:generateContent?key=${GEMINI_API_KEY}`,
          { 'Content-Type': 'application/json' },
          { contents: [{ parts: [{ text: query }] }], tools: [{ google_search: {} }] }
        );
        if (fallback.status === 200) return parseGeminiNativeResponse(fallback.body, fallbackModel);
        console.log(`[gemini] Fallback model also rate limited (${fallback.status}) — waiting 30s...`);
      } else {
        console.log('[gemini] Rate limited (429) — waiting 30s then retrying...');
      }
      await new Promise(r => setTimeout(r, 30000));
      const retry = await rawHttpPost(
        'generativelanguage.googleapis.com',
        `/v1beta/models/${geminiModel}:generateContent?key=${GEMINI_API_KEY}`,
        { 'Content-Type': 'application/json' },
        { contents: [{ parts: [{ text: query }] }], tools: [{ google_search: {} }] }
      );
      if (retry.status !== 200) {
        console.log(`[gemini] Retry also failed (${retry.status}) — falling through to Portkey`);
      } else {
        return parseGeminiNativeResponse(retry.body, geminiModel);
      }
    } else if (result.status === 200) {
      return parseGeminiNativeResponse(result.body, geminiModel);
    } else {
      console.log(`[gemini] Direct API error ${result.status}: ${JSON.stringify(result.body?.error || result.body).slice(0, 200)}`);
      console.log('[gemini] Falling back to Portkey...');
    }
  }

  // ── Attempt 2: Portkey SDK ─────────────────────────────────────────────────
  // Note: Portkey also routes to Google so may hit the same quota — skip if already 429
  console.log('[gemini] Trying Portkey SDK (note: same Google quota applies)...');
  const portkey = new Portkey({
    apiKey: PORTKEY_API_KEY,
    provider: PLATFORM_DEFAULTS.gemini.provider,
    customHeaders: { 'strict-openai-compliance': 'false' },
  });

  let sdkResponse;
  try {
    sdkResponse = await portkey.chat.completions.create({
      model,
      messages: [{ role: 'user', content: query }],
      tools: [{ googleSearch: {} }],
    });
  } catch {
    sdkResponse = await portkey.chat.completions.create({
      model,
      messages: [{ role: 'user', content: query }],
    });
  }

  const answer = sdkResponse.choices?.[0]?.message?.content || '';
  const sdkGm  = sdkResponse.groundingMetadata || sdkResponse.choices?.[0]?.message?.groundingMetadata || null;
  if (sdkGm?.groundingChunks?.length) {
    console.log('[gemini] groundingMetadata found via Portkey SDK ✓');
    return { answer, sources: extractGeminiCitations(sdkGm), raw: sdkResponse };
  }

  // ── Attempt 3: Raw HTTP via Portkey ───────────────────────────────────────
  console.log('[gemini] groundingMetadata absent in SDK — falling back to raw Portkey HTTP...');
  const rawResult = await rawHttpPost(
    'api.portkey.ai',
    '/v1/chat/completions',
    {
      'Content-Type': 'application/json',
      'x-portkey-api-key': PORTKEY_API_KEY,
      'x-portkey-provider': PLATFORM_DEFAULTS.gemini.provider,
      'strict-openai-compliance': 'false',
    },
    { model, messages: [{ role: 'user', content: query }], tools: [{ googleSearch: {} }] }
  );

  const rawBody = rawResult.body;
  const rawGm   = rawBody.groundingMetadata || rawBody.candidates?.[0]?.groundingMetadata || rawBody.choices?.[0]?.message?.groundingMetadata || null;
  const sources = extractGeminiCitations(rawGm);
  if (rawGm) {
    console.log(`[gemini] Portkey raw HTTP: ${sources.length} grounding chunks`);
  } else {
    console.log('[gemini] groundingMetadata absent even in raw Portkey HTTP — grounding not enabled on virtual key');
  }
  return { answer, sources, raw: rawBody };
}

function parseGeminiNativeResponse(body, model) {
  const text   = body.candidates?.[0]?.content?.parts?.map(p => p.text).join('') || '';
  const gm     = body.candidates?.[0]?.groundingMetadata || null;
  const sources = extractGeminiCitations(gm);
  if (gm) {
    console.log(`[gemini] Direct API ✓ — ${sources.length} grounding chunks`);
    if (gm.webSearchQueries?.length) console.log(`[gemini] Searched for: ${gm.webSearchQueries.join(', ')}`);
  } else {
    console.log('[gemini] Direct API returned no groundingMetadata');
  }
  return { answer: text, sources, raw: { ...body, model } };
}

// ── Main ──────────────────────────────────────────────────────────────────────
async function main() {
  const args = parseArgs(process.argv);
  const cfg  = PLATFORM_DEFAULTS[args.platform];

  if (!cfg) {
    console.error(`Unknown platform "${args.platform}". Choose: chatgpt | perplexity | gemini`);
    process.exit(1);
  }

  const model = args.model || cfg.model;

  console.log('\n=== GEO Query Test ===');
  console.log(`Platform : ${args.platform}`);
  console.log(`Model    : ${model}`);
  console.log(`Query    : ${args.query}\n`);

  try {
    let result;
    if      (args.platform === 'chatgpt')    result = await runChatGPT(args.query, model);
    else if (args.platform === 'perplexity') result = await runPerplexity(args.query, model);
    else if (args.platform === 'gemini')     result = await runGemini(args.query, model);

    // ── Answer ────────────────────────────────────────────────────────────────
    console.log('=== Answer ===');
    console.log(result.answer || '(empty)');

    // ── Citations ─────────────────────────────────────────────────────────────
    console.log('\n=== Citations ===');
    if (result.sources.length === 0) {
      console.log('(none found)');
      if (result.note) console.log('Note:', result.note);
      // Compact debug dump
      const rawStr = JSON.stringify(result.raw, null, 2);
      console.log('\n[debug] raw keys:', Object.keys(result.raw || {}));
      console.log('[debug] raw (first 1500 chars):\n', rawStr.slice(0, 1500));
    } else {
      result.sources.forEach((s, i) =>
        console.log(`[${i + 1}] ${s.title || '(no title)'}\n    ${s.url}`)
      );
    }

    // ── Model routing ─────────────────────────────────────────────────────────
    console.log('\n=== Actual model routed ===');
    console.log(result.raw?.model || result.raw?.provider || '(not present)');

  } catch (err) {
    console.error('\n=== ERROR ===');
    console.error(err.message);
  }
}

main();
