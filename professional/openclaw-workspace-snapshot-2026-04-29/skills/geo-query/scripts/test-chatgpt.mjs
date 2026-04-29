/**
 * test-chatgpt.mjs
 * Quick test: GPT via Portkey Responses API with web_search_preview tool.
 * Model: gpt-4o-mini-search-preview (Chat Completions with web search)
 * Provider: @azure-openai-bbfaac
 */

import { Portkey } from 'portkey-ai';

const PORTKEY_API_KEY = 'VwFslTtBMP/j3m4i/HkmvyEv/mlR';
const QUERY = 'What is formative assessment in education? Look up online';

const portkey = new Portkey({
  apiKey: PORTKEY_API_KEY,
  provider: '@azure-openai-bbfaac',
});

async function main() {
  console.log(`\nQuerying via Portkey Responses API...`);
  console.log(`Provider: @azure-openai-bbfaac`);
  console.log(`Model: gpt-4o-mini-search-preview`);
  console.log(`Query: ${QUERY}\n`);

  try {
    // Responses API (as per reference snippet pattern)
    const response = await portkey.responses.create({
      model: 'gpt-5-mini',
      tools: [{ type: 'web_search_preview' }],
      input: QUERY,
    });

    console.log('=== Raw response keys ===');
    console.log(Object.keys(response));

    console.log('\n=== output_text ===');
    console.log(response.output_text || '(empty)');

    console.log('\n=== output[] ===');
    console.log(JSON.stringify(response.output, null, 2));

    // Extract citations from annotations
    const sources = [];
    if (response.output) {
      for (const block of response.output) {
        if (block.content) {
          for (const item of block.content) {
            if (item.annotations) {
              for (const ann of item.annotations) {
                if (ann.type === 'url_citation') {
                  // GPT Responses API: url + title directly on ann
                  // older shape: nested under ann.url_citation
                  const url = ann.url || ann.url_citation?.url;
                  const title = ann.title || ann.url_citation?.title || '';
                  if (url && !sources.find(s => s.url === url)) {
                    sources.push({ url, title });
                  }
                }
              }
            }
          }
        }
      }
    }

    console.log('\n=== Extracted citations ===');
    if (sources.length === 0) {
      console.log('(none found)');
    } else {
      sources.forEach((s, i) => console.log(`[${i+1}] ${s.title}\n    ${s.url}`));
    }

    console.log('\n=== model field (to confirm actual routing) ===');
    console.log(response.model || '(not present)');

  } catch (err) {
    console.error('\n=== ERROR ===');
    console.error(err.message);
    if (err.response) {
      console.error('Status:', err.status);
      console.error('Body:', JSON.stringify(err.response, null, 2));
    }
  }
}

main();
