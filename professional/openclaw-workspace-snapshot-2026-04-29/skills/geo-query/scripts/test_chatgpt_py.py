import urllib.request, urllib.error, json

url = "https://api.portkey.ai/v1/responses"
body = json.dumps({
    "model": "gpt-5-mini",
    "tools": [{"type": "web_search_preview"}],
    "input": "what is formative assessment?",
}).encode()

req = urllib.request.Request(url, data=body, method="POST")
req.add_header("Content-Type", "application/json")
req.add_header("Content-Length", str(len(body)))
req.add_header("User-Agent", "Mozilla/5.0 (compatible; WaymarkBot/1.0)")
req.add_header("x-portkey-api-key", "VwFslTtBMP/j3m4i/HkmvyEv/mlR")
req.add_header("x-portkey-provider", "@azure-openai-bbfaac")

try:
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read()
        parsed = json.loads(raw.decode("utf-8"))
        print("model:", parsed.get("model"))
        print("provider:", parsed.get("provider"))
        output = parsed.get("output", [])
        print("output blocks:", len(output))
        urls = []
        for block in output:
            for item in block.get("content", []):
                for ann in item.get("annotations", []):
                    if ann.get("type") == "url_citation":
                        u = ann.get("url") or (ann.get("url_citation") or {}).get("url")
                        if u: urls.append(u)
        print("citations:", urls)
        # print full output for inspection
        print("\nfull output:")
        print(json.dumps(output, indent=2)[:2000])
except Exception as e:
    print("Error:", e)
