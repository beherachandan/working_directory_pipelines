"""
Webflow CMS publisher.

Setup:
1. Set WEBFLOW_API_TOKEN and WEBFLOW_SITE_ID in .env
2. Run: python orchestrator.py webflow-setup  (lists collection IDs)
3. Fill in collection IDs in .env for each cluster
4. Run: python orchestrator.py webflow-publish-single 52  (test one article)
5. Run: python orchestrator.py webflow-publish --mode draft  (all articles)

Webflow API v2 docs: https://developers.webflow.com/v2.0.0/reference
"""
import json
import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

WEBFLOW_API_BASE = "https://api.webflow.com/v2"

WEBFLOW_PROGRESS_FILE = Path(__file__).parent.parent / "outputs" / "webflow_progress.json"


class WebflowPublisher:
    """Webflow CMS publisher using Webflow API v2."""

    CLUSTER_TO_COLLECTION_ENV = {
        "Differentiated Learning": "WEBFLOW_COLLECTION_DIFFERENTIATED_LEARNING",
        "Scaffolding": "WEBFLOW_COLLECTION_SCAFFOLDING",
        "Engagement": "WEBFLOW_COLLECTION_ENGAGEMENT",
    }

    def __init__(self, api_token: str = "", site_id: str = "", collections: dict = None):
        self.api_token = api_token
        self.site_id = site_id
        self.collections = collections or {}
        self.enabled = bool(api_token and site_id)

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
            "accept": "application/json",
        }

    async def list_collections(self) -> list[dict]:
        """Fetch all CMS collections for the configured site."""
        if not self.enabled:
            return []
        import aiohttp
        url = f"{WEBFLOW_API_BASE}/sites/{self.site_id}/collections"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self._headers()) as resp:
                resp.raise_for_status()
                data = await resp.json()
                return data.get("collections", [])

    def get_collection_id(self, cluster: str) -> str:
        """Return the Webflow collection ID for a given cluster name."""
        return self.collections.get(cluster, "")

    @staticmethod
    def _md_to_html(md_text: str) -> str:
        """Convert markdown to HTML for Webflow Rich Text field."""
        try:
            import markdown as md_lib
            return md_lib.markdown(
                md_text,
                extensions=["tables", "fenced_code", "sane_lists"],
            )
        except ImportError:
            # Fallback: basic conversion without the markdown package
            html = md_text
            # Headings
            for level in range(6, 0, -1):
                pattern = r"^" + "#" * level + r"\s+(.+)$"
                html = re.sub(pattern, rf"<h{level}>\1</h{level}>", html, flags=re.MULTILINE)
            # Bold + italic
            html = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", html)
            html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
            html = re.sub(r"\*(.+?)\*", r"<em>\1</em>", html)
            # Bullet lists (basic)
            html = re.sub(r"^[-*]\s+(.+)$", r"<li>\1</li>", html, flags=re.MULTILINE)
            html = re.sub(r"(<li>.*</li>)", r"<ul>\1</ul>", html, flags=re.DOTALL)
            # Paragraphs
            parts = re.split(r"\n{2,}", html)
            html = "\n".join(
                f"<p>{p.strip()}</p>" if not p.strip().startswith("<") else p.strip()
                for p in parts if p.strip()
            )
            return html

    def _build_item_fields(self, result: dict, enhanced_md: str) -> dict:
        """
        Map ArticleResult fields to Webflow CMS item fieldData.
        Field names must match exactly what's configured in the Webflow Designer.
        """
        checklist = result.get("pre_publish_checklist", {})
        platform_flags = result.get("platform_flags", {})
        schema_list = checklist.get("schema_to_add", [])
        if isinstance(schema_list, list):
            schema_str = ", ".join(schema_list)
        else:
            schema_str = str(schema_list)

        # Slug: prefer slug_recommendation, fallback to url_slug, then slugify name
        slug = (
            checklist.get("slug_recommendation")
            or result.get("url_slug")
            or re.sub(r"[^a-z0-9]+", "-", result.get("name", "article").lower()).strip("-")
        )

        body_html = self._md_to_html(enhanced_md) if enhanced_md else ""

        fields = {
            "name": result.get("name", ""),
            "slug": slug,
            "body": body_html,
            "seo-title": checklist.get("title_tag", ""),
            "seo-description": checklist.get("meta_description", ""),
            "geo-score": float(result.get("geo_composite", 0) or 0),
            "brand-verdict": result.get("brand_verdict", ""),
            "sub-cluster": result.get("sub_cluster", ""),
            "schema-markup": schema_str,
            "aio-ready": bool(platform_flags.get("aio_ready")),
            "chatgpt-ready": bool(platform_flags.get("chatgpt_ready")),
        }
        # Strip empty strings for optional fields
        return {k: v for k, v in fields.items() if v != ""}

    async def _create_item(self, session, collection_id: str, fields: dict) -> str:
        """Create a draft CMS item. Returns item_id."""
        url = f"{WEBFLOW_API_BASE}/collections/{collection_id}/items"
        payload = {"fieldData": fields}
        async with session.post(url, headers=self._headers(), json=payload) as resp:
            if resp.status not in (200, 201):
                body = await resp.text()
                raise RuntimeError(f"Create item failed ({resp.status}): {body[:300]}")
            data = await resp.json()
            return data.get("id") or data.get("_id") or data["items"][0]["id"]

    async def _publish_item(self, session, collection_id: str, item_id: str):
        """Publish a draft CMS item live."""
        url = f"{WEBFLOW_API_BASE}/collections/{collection_id}/items/{item_id}/live"
        async with session.put(url, headers=self._headers(), json={}) as resp:
            if resp.status not in (200, 202):
                body = await resp.text()
                raise RuntimeError(f"Publish item failed ({resp.status}): {body[:300]}")

    async def publish_article(
        self,
        result: dict,
        enhanced_md: str = "",
        mode: str = "draft",
    ) -> dict:
        """
        Publish one article to Webflow CMS.

        mode="draft"  → create draft only
        mode="live"   → create draft then publish live

        Returns: {status, item_id, item_url, collection_id, error}
        """
        if not self.enabled:
            return {
                "status": "skipped",
                "error": "Webflow not configured — set WEBFLOW_API_TOKEN and WEBFLOW_SITE_ID in .env",
            }

        cluster = result.get("cluster", "")
        collection_id = self.get_collection_id(cluster)
        if not collection_id:
            return {
                "status": "failed",
                "error": f"No collection ID configured for cluster '{cluster}'. Run webflow-setup and fill .env.",
            }

        fields = self._build_item_fields(result, enhanced_md)
        if not fields.get("name"):
            return {"status": "failed", "error": "Article has no name — cannot publish"}

        import aiohttp
        try:
            async with aiohttp.ClientSession() as session:
                item_id = await self._create_item(session, collection_id, fields)
                logger.info(f"  Created draft item {item_id} for '{fields['name']}'")

                if mode == "live":
                    await self._publish_item(session, collection_id, item_id)
                    logger.info(f"  Published live: {item_id}")
                    status = "live"
                else:
                    status = "draft"

            item_url = f"https://webflow.com/design/{self.site_id}/cms/{collection_id}/{item_id}"
            return {
                "status": status,
                "item_id": item_id,
                "collection_id": collection_id,
                "item_url": item_url,
            }

        except Exception as e:
            logger.error(f"  Webflow publish failed for #{result.get('item_num')}: {e}")
            return {"status": "failed", "error": str(e)}

    def get_field_mapping(self) -> dict:
        """Reference: Webflow CMS field → ArticleResult path mapping."""
        return {
            "name": "name",
            "slug": "pre_publish_checklist.slug_recommendation",
            "body": "<enhanced_md converted to HTML>",
            "seo-title": "pre_publish_checklist.title_tag",
            "seo-description": "pre_publish_checklist.meta_description",
            "geo-score": "geo_composite",
            "brand-verdict": "brand_verdict",
            "sub-cluster": "sub_cluster",
            "schema-markup": "pre_publish_checklist.schema_to_add (joined)",
            "aio-ready": "platform_flags.aio_ready",
            "chatgpt-ready": "platform_flags.chatgpt_ready",
        }


# ─── Progress tracking ────────────────────────────────────────────────────────

def load_webflow_progress() -> dict:
    if WEBFLOW_PROGRESS_FILE.exists():
        with open(WEBFLOW_PROGRESS_FILE) as f:
            return json.load(f)
    return {}


def save_webflow_progress(progress: dict):
    tmp = WEBFLOW_PROGRESS_FILE.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(progress, f, indent=2)
    tmp.replace(WEBFLOW_PROGRESS_FILE)
