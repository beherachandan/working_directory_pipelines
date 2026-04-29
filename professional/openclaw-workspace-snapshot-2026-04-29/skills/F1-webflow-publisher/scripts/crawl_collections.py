"""
crawl_collections.py — List all articles in every /learn/ collection
Usage: python3 crawl_collections.py
Output: prints a table + writes crawl_results.json
"""
import asyncio
import json
import sys
from datetime import datetime, timezone

try:
    import aiohttp
except ImportError:
    print("ERROR: aiohttp not installed. Run: pip install aiohttp")
    sys.exit(1)

WEBFLOW_API_TOKEN = "de4f365546bd477f108d9e2434dc1c2e2fd1b958aea9d3af34ecbf72d0a0daf1"
WEBFLOW_API_BASE  = "https://api.webflow.com/v2"

ALL_COLLECTIONS = {
    "subjects-card":           "68482ad1b68f89d314c451b3",
    "testimonials":            "6848645fd8fed2bf449d0bda",
    "blog":                    "6849f74f12a3a2d481991656",
    "blog-categories":         "684ae6ff51e257616de5adf1",
    "authors":                 "684aea77b097cc8a0ddb57a2",
    "student-testimonials":    "685025dd9af24d8a10196410",
    "faqs":                    "6850473a6fb75a92cada401b",
    "faq-categories":          "685341ad1845448abc5bd16a",
    "career-social-cards":     "6880e7e0cdd45194ec3a4cc2",
    "news-article":            "6897940180f51af6ea64510c",
    "webinar":                 "689d9ff865089a71ad09cf36",
    "k12teacher":              "6915b9f881ab8e15025de2a7",
    "teachers-categories":     "6915bc51a853b4e2d11ee85a",
    "business-testimonial":    "69395e3904787d9ca8831076",
    "assessments":             "6966367badfd2734b4e708c2",
    "lesson-plan":             "696e0ecfd20021b0ba12ef08",
    "learn-category":          "696e1255d744309a5f0aa34e",
    "education-assessment":    "69722f178db818ab468d8701",
    "generators":              "69722f2d64a2cc8327352307",
    "question-types":          "69722f7dd5ea1f81a678f394",
    "reviewer":                "699d9a30d3993cd65be117a3",
    "solutions":               "69a1cb1b84742b1bce913a20",
    "cte-blogs":               "69c4fb4ba301227729ff47f9",
    "cte-certification-prep":  "69c59a47c8c0deac2f2f79e5",
    "cte-compare":             "69c59a5376bd1cd02ca7e8fb",
    "cte-perkins-v":           "69c59a5f00023845a7a7ce70",
    "cte-state-standards":     "69c59a6f3e335d309963b417",
    "differentiated-learning": "69ca46c801a5a26e0c8d8f22",
    "scaffolding":             "69e1d89aa44857542a0259b7",
    "engagement":              "69e1d89aa44857542a025a00",
}

HEADERS = {
    "Authorization": f"Bearer {WEBFLOW_API_TOKEN}",
    "accept": "application/json",
}

async def fetch_items(session, collection_id: str, slug: str) -> list:
    items = []
    offset = 0
    limit  = 100
    while True:
        url = f"{WEBFLOW_API_BASE}/collections/{collection_id}/items?offset={offset}&limit={limit}"
        async with session.get(url, headers=HEADERS) as resp:
            if resp.status != 200:
                body = await resp.text()
                print(f"  ERROR {resp.status} on {slug}: {body[:200]}")
                break
            data = await resp.json()
        batch = data.get("items", [])
        items.extend(batch)
        total = data.get("pagination", {}).get("total", len(items))
        offset += len(batch)
        if offset >= total or not batch:
            break
    return items

async def main():
    results = {}
    async with aiohttp.ClientSession() as session:
        for slug, cid in ALL_COLLECTIONS.items():
            print(f"\nFetching /{slug} ({cid})...")
            items = await fetch_items(session, cid, slug)
            results[slug] = {
                "collection_id": cid,
                "count": len(items),
                "items": [
                    {
                        "name":        i.get("fieldData", {}).get("name", i.get("fieldData", {}).get("title", "?")),
                        "slug":        i.get("fieldData", {}).get("slug", "?"),
                        "id":          i.get("id", "?"),
                        "published":   i.get("isArchived") == False and i.get("isDraft") == False,
                        "draft":       i.get("isDraft", False),
                        "archived":    i.get("isArchived", False),
                        "lastUpdated": i.get("lastUpdated", ""),
                    }
                    for i in items
                ],
            }
            print(f"  → {len(items)} items")

    # Print full table
    print("\n" + "="*100)
    print(f"{'COLLECTION':<30} {'ID':<26} {'COUNT':>5}  {'ITEM NAME':<45} SLUG")
    print("="*100)
    total_articles = 0
    for slug, data in results.items():
        count = data["count"]
        total_articles += count
        if count == 0:
            print(f"/{slug:<29} {data['collection_id']:<26} {count:>5}  (empty)")
        for idx, item in enumerate(data["items"]):
            col_display = f"/{slug}" if idx == 0 else ""
            cid_display = data['collection_id'] if idx == 0 else ""
            cnt_display = str(count) if idx == 0 else ""
            print(f"{col_display:<30} {cid_display:<26} {cnt_display:>5}  {item['name'][:45]:<45} {item['slug']}")
    print("="*100)
    print(f"{'TOTAL':<30} {'':26} {total_articles:>5}")

    # Write JSON with proper name
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    out_path = f"webflow-collections-index-{timestamp}.json"
    with open(out_path, "w") as f:
        json.dump({
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "site_id": "68355113496452bf05789e95",
            "total_collections": len(results),
            "total_items": total_articles,
            "collections": results,
        }, f, indent=2)
    print(f"\nFull index written to: {out_path}")

if __name__ == "__main__":
    asyncio.run(main())
