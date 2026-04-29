#!/usr/bin/env node
/**
 * geo-query.js — GEO Query Intelligence
 * Queries generative AI platforms via Portkey, captures answer + cited sources.
 *
 * Supported platforms:
 *   chatgpt    — OpenAI GPT via Azure (Responses API + web_search_preview)
 *   perplexity — Perplexity Sonar (Chat API, citations[] in response)
 *   gemini     — Google Gemini via Vertex AI (Chat API + google_search grounding)
 *   claude     — Anthropic Claude via AWS Bedrock (Chat API + web_search tool)
 *
 * Usage:
 *   node geo-query.js --query "what is formative assessment" --platforms chatgpt,perplexity,gemini
 *   node geo-query.js --batch references/calibration-queries.json --platforms chatgpt,perplexity
 *   node geo-query.js --query "..." --platforms all
 *   node geo-query.js --batch ... --output memory/research/geo-runs/2026-04-22-run.json
 *
 * Env vars:
 *   PORTKEY_API_KEY   (required)
 *   WAYGROUND_DOMAIN  (default: wayground.com)
 */

import { Portkey } from 'portkey-ai';
import fs from 'fs/promises';
import path from 'path';
import { parseArgs } from 'util';

// ─── Config ───────────────────────────────────────────────────────────────────

const PORTKEY_API_KEY = process.env.PORTKEY_API_KEY;
if (!PORTKEY_API_KEY) {
  console.error('ERROR: PORTKEY_API_KEY env var not set.\nRun: export PORTKEY_API_KEY="your_key"');
  process.exit(1);
}
const WAYGROUND_DOMAIN = process.env.WAYGROUND_DOMAIN || 'wayground.com';
let DEBUG = false;

/**
 * Platform definitions.
 * provider: Portkey virtual key slug — update if your account uses different slugs.
 * model: model name passed to the API.
 * api: which API type to use ('responses' = OpenAI Responses API, 'chat' = Chat Completions)
 */
const PLATFORMS = {
  //
  // API keys:
  //   OLD key (UgKiRSUEFAHGSTWBjOQNXDwkKKj/) — default routes to Claude Sonnet 4.6 via Bedrock
  //   NEW key (VwFslTtBMP/j3m4i/HkmvyEv/mlR) — configurable, pass any model; use for GPT/Gemini/Perplexity
  //
  // Use PORTKEY_API_KEY_NEW env var for platforms that need real GPT/Gemini/Perplexity.
  //

  // GPT via Portkey Responses API (web_search_preview — returns url_citation annotations)
  chatgpt: {
    label: 'GPT-5-mini (Responses API)',
    provider: '@azure-openai-bbfaac',
    model: 'gpt-5-mini',
    api: 'responses',
    apiKeyOverride: 'new', // use PORTKEY_API_KEY_NEW
  },

  // Perplexity Sonar via Chat Completions (native citations[] in response)
  perplexity: {
    label: 'Perplexity Sonar',
    provider: '@perplexity-ai/sonar',
    model: 'sonar',
    api: 'chat',
    apiKeyOverride: 'new',
    customHeaders: { 'strict-openai-compliance': 'false' },
  },

  // Gemini via Chat Completions + google_search grounding
  gemini: {
    label: 'Gemini (Grounded)',
    provider: '@content-rnd-gem-565e6c',
    model: 'gemini-2.0-flash-001',
    api: 'chat',
    apiKeyOverride: 'new',
    customHeaders: { 'strict-openai-compliance': 'false' },
    tool: { type: 'function', function: { name: 'google_search', parameters: { type: 'object', properties: {} } } },
  },

  // Claude answer-quality (no citations — Bedrock, old key)
  claude: {
    label: 'Claude Sonnet 4.6 (Bedrock)',
    provider: '@aws-us-east-1',
    model: 'anthropic.claude-3-5-sonnet-20241022-v2:0',
    api: 'chat',
    tool: null,
  },

  // Claude with Tavily-powered web search (multi-turn, produces source URLs)
  claude_search: {
    label: 'Claude + Tavily Search',
    provider: '@aws-us-east-1',
    model: 'anthropic.claude-3-5-sonnet-20241022-v2:0',
    api: 'chat_search',
    tool: null,
  },
};

// Active platforms for --platforms all
const ALL_PLATFORMS = ['chatgpt', 'gemini', 'perplexity', 'claude_search'];

// New Portkey API key (configurable routing — GPT/Gemini/Perplexity)
const PORTKEY_API_KEY_NEW = process.env.PORTKEY_API_KEY_NEW || 'VwFslTtBMP/j3m4i/HkmvyEv/mlR';

function getApiKey(config) {
  return config.apiKeyOverride === 'new' ? PORTKEY_API_KEY_NEW : PORTKEY_API_KEY;
}

// ─── Platform Queriers ────────────────────────────────────────────────────────

/**
 * ChatGPT via OpenAI Responses API.
 * Sources: output[].content[].annotations[type=url_citation].{url, title}
 * Max data: search_context_size='high' gives most comprehensive results.
 */
async function queryChatGPT(query, config) {
  const portkey = new Portkey({ apiKey: getApiKey(config), provider: config.provider });

  // Use Responses API — returns output_text + url_citation annotations
  const response = await portkey.responses.create({
    model: config.model,
    tools: [{ type: 'web_search_preview' }],
    input: query,
  });

  if (DEBUG) process.stderr.write(`\n[DEBUG chatgpt raw]\n${JSON.stringify(response, null, 2)}\n`);

  const content = response.output_text || '';
  const sources = [];

  // Responses API: annotations live on output[].content[].annotations
  // Shape: { type: 'url_citation', url: '...', title: '...', start_index, end_index }
  for (const block of (response.output || [])) {
    for (const item of (block.content || [])) {
      for (const ann of (item.annotations || [])) {
        if (ann.type === 'url_citation') {
          const url = ann.url || ann.url_citation?.url;
          const title = ann.title || ann.url_citation?.title || '';
          if (url && !sources.find(s => s.url === url)) {
            sources.push({ url, title, position: sources.length + 1 });
          }
        }
      }
    }
  }

  // Fallback: parse markdown links from output_text if annotations[] was empty
  // gpt-5-mini sometimes embeds citations as [title](url) in text instead of annotations
  if (sources.length === 0 && content) {
    const mdLinkRe = /\[([^\]]+)\]\((https?:\/\/[^)]+)\)/g;
    let match;
    while ((match = mdLinkRe.exec(content)) !== null) {
      const [, title, url] = match;
      if (!sources.find(s => s.url === url)) {
        sources.push({ url, title, position: sources.length + 1 });
      }
    }
  }

  return buildResult(content, sources, {
    raw_source_count: sources.length,
    model: response.model || config.model,
    api: 'responses',
  });
}

/**
 * Perplexity Sonar via Chat Completions.
 * Sources: response.citations[] — array of URL strings.
 * Max data: sonar-pro gives richer citations than sonar.
 * Requires strict-openai-compliance: false to expose non-standard fields.
 *
 * Full response also includes:
 *   response.usage.citation_tokens
 *   response.search_results[] (if available on pro tier) — richer than citations[]
 */
async function queryPerplexity(query, config) {
  const portkey = new Portkey({
    apiKey: getApiKey(config),
    provider: config.provider,
    customHeaders: config.customHeaders,
  });

  const response = await portkey.chat.completions.create({
    model: config.model,
    messages: [{ role: 'user', content: query }],
  });

  const content = response.choices?.[0]?.message?.content || '';

  // Primary: citations[] array — URL strings
  const citationUrls = response.citations || [];

  // Secondary: search_results[] if available (Sonar Pro tier)
  // Format: [{url, title, date, last_updated}]
  const searchResults = response.search_results || [];

  const sources = searchResults.length > 0
    ? searchResults.map((r, i) => ({ url: r.url, title: r.title || '', date: r.date || '', position: i + 1 }))
    : citationUrls.map((url, i) => ({ url, title: '', position: i + 1 }));

  return buildResult(content, sources, {
    raw_source_count: sources.length,
    model: config.model,
    usage: response.usage || {},
    api: 'chat',
  });
}

/**
 * Gemini via Chat Completions + google_search grounding tool.
 * Sources: response.groundingMetadata.groundingChunks[].web.{uri, title}
 *
 * Note: Portkey docs flag SDK grounding as experimental.
 * If groundingMetadata absent, we attempt to parse inline [N] citation markers
 * as a fallback signal.
 *
 * Max data from grounding:
 *   groundingChunks[]        — source URLs + titles
 *   groundingSupports[]      — maps text segments → chunk indices (inline citation positions)
 *   webSearchQueries[]       — what Gemini actually searched for
 *   searchEntryPoint.renderedContent — HTML of "Search" suggestions
 */
async function queryGemini(query, config) {
  const portkey = new Portkey({
    apiKey: getApiKey(config),
    provider: config.provider,
    customHeaders: config.customHeaders,
  });

  // Try with google_search tool first; fall back to no-tool if it fails
  let response;
  try {
    response = await portkey.chat.completions.create({
      model: config.model,
      messages: [{ role: 'user', content: query }],
      tools: [config.tool],
    });
  } catch (toolErr) {
    if (DEBUG) process.stderr.write(`\n[DEBUG gemini tool failed: ${toolErr.message}] retrying without tool\n`);
    response = await portkey.chat.completions.create({
      model: config.model,
      messages: [{ role: 'user', content: query }],
    });
  }

  if (DEBUG) process.stderr.write(`\n[DEBUG gemini raw]\n${JSON.stringify(response, null, 2)}\n`);

  const content = response.choices?.[0]?.message?.content || '';

  // Primary path: groundingMetadata (may be absent if Portkey SDK strips it)
  const gm = response.groundingMetadata || response.candidates?.[0]?.groundingMetadata || {};
  const chunks = gm.groundingChunks || [];
  const supports = gm.groundingSupports || [];
  const searchQueries = gm.webSearchQueries || [];

  const sources = chunks
    .map((chunk, i) => ({
      url: chunk.web?.uri || '',
      title: chunk.web?.title || '',
      position: i + 1,
    }))
    .filter(s => s.url);

  // Build inline citation map: text position → source URLs
  const inlineCitations = supports.map(s => ({
    text_segment: content.slice(s.segment?.startIndex || 0, s.segment?.endIndex || 0),
    source_urls: (s.groundingChunkIndices || []).map(i => chunks[i]?.web?.uri).filter(Boolean),
  }));

  const grounded = sources.length > 0;

  return buildResult(content, sources, {
    raw_source_count: sources.length,
    model: config.model,
    grounded,
    search_queries_used: searchQueries,
    inline_citations: inlineCitations,
    api: 'chat',
    note: grounded ? null : 'groundingMetadata absent — Portkey SDK may not expose grounding fields. Try direct Vertex AI if needed.',
  });
}

/**
 * Claude via AWS Bedrock.
 * Claude doesn't return inline citations like the others.
 * Web search is a tool_use call — we capture tool inputs (what it searched for)
 * and tool results (what it found) as source signals.
 *
 * For GEO purposes this is less useful than Perplexity/Gemini/ChatGPT
 * but included for completeness.
 */
async function queryClaude(query, config) {
  const portkey = new Portkey({
    apiKey: PORTKEY_API_KEY,
    provider: config.provider,
  });

  // Only include tools if defined for this platform
  const requestBody = {
    model: config.model,
    messages: [{ role: 'user', content: query }],
  };
  if (config.tool) requestBody.tools = [config.tool];

  const response = await portkey.chat.completions.create(requestBody);

  if (DEBUG) process.stderr.write(`\n[DEBUG claude raw]\n${JSON.stringify(response, null, 2)}\n`);

  const content = response.choices?.[0]?.message?.content || '';
  const toolCalls = response.choices?.[0]?.message?.tool_calls || [];

  const searchQueries = toolCalls
    .filter(t => t.function?.name === 'web_search')
    .map(t => { try { return JSON.parse(t.function.arguments)?.query; } catch { return null; } })
    .filter(Boolean);

  return buildResult(content, [], {
    model: config.model,
    note: 'Claude — answer quality only, no inline citations via this route.',
    search_queries_issued: searchQueries,
    api: 'chat',
  });
}

/**
 * Claude + Tavily multi-turn search.
 * Step 1: Ask Claude what to search for.
 * Step 2: Run Tavily search with that query.
 * Step 3: Feed results back to Claude, get grounded answer + source URLs.
 * This gives us real cited sources even without native Gemini/Perplexity access.
 */
async function queryClaudeSearch(query, config) {
  const TAVILY_API_KEY = process.env.TAVILY_API_KEY;
  if (!TAVILY_API_KEY) {
    return buildResult('', [], {
      model: config.model,
      note: 'TAVILY_API_KEY not set. Run: export TAVILY_API_KEY="your_key"',
      api: 'chat_search',
    });
  }

  const portkey = new Portkey({ apiKey: PORTKEY_API_KEY, provider: config.provider });

  // Step 1: Run Tavily search
  const tavilyRes = await fetch('https://api.tavily.com/search', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      api_key: TAVILY_API_KEY,
      query,
      search_depth: 'advanced',
      max_results: 8,
      include_answer: false,
    }),
  });
  const tavilyData = await tavilyRes.json();
  const searchResults = tavilyData.results || [];

  // Step 2: Format results for Claude
  const searchContext = searchResults.map((r, i) =>
    `[${i+1}] ${r.title}\nURL: ${r.url}\n${r.content?.slice(0, 400)}`
  ).join('\n\n');

  // Step 3: Ask Claude to answer using search results
  const response = await portkey.chat.completions.create({
    model: config.model,
    messages: [
      {
        role: 'user',
        content: `Answer this question using the search results below. Cite sources by number [1], [2] etc.\n\nQuestion: ${query}\n\nSearch Results:\n${searchContext}`
      }
    ],
  });

  if (DEBUG) process.stderr.write(`\n[DEBUG claude_search raw]\n${JSON.stringify(response, null, 2)}\n`);

  const content = response.choices?.[0]?.message?.content || '';

  // Extract cited source numbers from answer ([1], [2] etc) and map to URLs
  const citedIndices = [...new Set([...content.matchAll(/\[(\d+)\]/g)].map(m => parseInt(m[1]) - 1))];
  const sources = citedIndices
    .filter(i => i >= 0 && i < searchResults.length)
    .map((i, pos) => ({
      url: searchResults[i].url,
      title: searchResults[i].title || '',
      position: pos + 1,
    }));

  // Also include all search results as background (not just cited ones)
  const allSearched = searchResults.map((r, i) => ({ url: r.url, title: r.title, position: i + 1 }));

  return buildResult(content, sources, {
    model: config.model,
    api: 'chat_search',
    all_searched_urls: allSearched,
    note: 'Claude + Tavily multi-turn. sources[] = explicitly cited. all_searched_urls[] = full search set.',
  });
}

// ─── Helpers ──────────────────────────────────────────────────────────────────

function buildResult(content, sources, meta = {}) {
  const waygroundSource = sources.find(s => s.url?.includes(WAYGROUND_DOMAIN));

  const domainCounts = {};
  for (const s of sources) {
    try {
      const domain = new URL(s.url).hostname.replace('www.', '');
      domainCounts[domain] = (domainCounts[domain] || 0) + 1;
    } catch {}
  }

  return {
    answer_snippet: content.slice(0, 500),
    answer_length_chars: content.length,
    sources,
    source_count: sources.length,
    wayground_cited: !!waygroundSource,
    wayground_position: waygroundSource?.position ?? null,
    top_cited_domains: domainCounts,
    ...meta,
  };
}

function parsePlatforms(input) {
  if (input === 'all') return ALL_PLATFORMS;
  return input.split(',').map(p => p.trim().toLowerCase()).filter(p => PLATFORMS[p]);
}

// ─── Runner ───────────────────────────────────────────────────────────────────

async function runQuery(query, platforms) {
  const result = { query, timestamp: new Date().toISOString(), results: {} };

  // Append lookup intent to help GPT/Gemini trigger web search + return citations
  const enrichedQuery = query.endsWith('?') || query.endsWith('.')
    ? query.slice(0, -1) + ' Look up online' + query.slice(-1)
    : query + ' Look up online';

  for (const platform of platforms) {
    const config = PLATFORMS[platform];
    process.stderr.write(`  → [${config.label}] "${query.slice(0, 60)}" ... `);
    try {
      if (platform === 'chatgpt')        result.results.chatgpt       = await queryChatGPT(enrichedQuery, config);
      else if (platform === 'claude')    result.results.claude        = await queryClaude(query, config);
      else if (platform === 'claude_search') result.results.claude_search = await queryClaudeSearch(enrichedQuery, config);
      else if (platform === 'perplexity') result.results.perplexity   = await queryPerplexity(enrichedQuery, config);
      else if (platform === 'gemini')    result.results.gemini        = await queryGemini(enrichedQuery, config);
      const r = result.results[platform];
      process.stderr.write(`✓ ${r.source_count} sources, wayground=${r.wayground_cited}\n`);
    } catch (err) {
      result.results[platform] = { error: err.message, stack: err.stack?.split('\n')[1] };
      process.stderr.write(`✗ ${err.message}\n`);
    }
  }
  return result;
}

// ─── Main ─────────────────────────────────────────────────────────────────────

async function main() {
  const { values } = parseArgs({
    options: {
      query:     { type: 'string' },
      batch:     { type: 'string' },
      platforms: { type: 'string', default: 'chatgpt' },
      output:    { type: 'string' },
      debug:     { type: 'boolean', default: false },
    },
  });

  DEBUG = values.debug || false;
  const platforms = parsePlatforms(values.platforms);
  if (platforms.length === 0) {
    console.error(`ERROR: No valid platforms. Choose from: ${ALL_PLATFORMS.join(', ')} or "all"`);
    process.exit(1);
  }

  process.stderr.write(`Platforms: ${platforms.map(p => PLATFORMS[p].label).join(', ')}\n\n`);

  const allResults = [];

  if (values.batch) {
    const raw = await fs.readFile(values.batch, 'utf8');
    const queries = JSON.parse(raw);
    for (const item of queries) {
      const query = typeof item === 'string' ? item : item.query;
      allResults.push(await runQuery(query, platforms));
    }
  } else if (values.query) {
    allResults.push(await runQuery(values.query, platforms));
  } else {
    console.error('ERROR: provide --query "..." or --batch path/to/queries.json');
    process.exit(1);
  }

  const output = allResults.length === 1 ? allResults[0] : allResults;

  if (values.output) {
    const outPath = path.resolve(values.output);
    await fs.mkdir(path.dirname(outPath), { recursive: true });
    await fs.writeFile(outPath, JSON.stringify(output, null, 2), 'utf8');
    console.error(`\n✓ Output written to ${outPath}`);
  } else {
    console.log(JSON.stringify(output, null, 2));
  }
}

main().catch(err => {
  console.error('Fatal:', err.message);
  process.exit(1);
});
