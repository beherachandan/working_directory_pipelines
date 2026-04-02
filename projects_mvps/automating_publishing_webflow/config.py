"""Central configuration for the evaluation pipeline."""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent

# --- Paths ---
XLSX_PATH = BASE_DIR / "Next_50_batch_fomo.xlsx"
OUTPUTS_DIR = BASE_DIR / "outputs"
ARTICLES_DIR = OUTPUTS_DIR / "articles"
CLUSTERS_DIR = OUTPUTS_DIR / "clusters"
PROGRESS_FILE = OUTPUTS_DIR / "progress.json"
SHARED_CONTEXT_DIR = BASE_DIR / "shared_context"
AGENTS_DIR = BASE_DIR / "agents"

# --- Models ---
GEO_MODEL = "claude-opus-4-6"
BRAND_MODEL = "claude-sonnet-4-6"
CLUSTER_MODEL = "claude-sonnet-4-6"
ENHANCER_MODEL = "claude-sonnet-4-6"
TEACHER_REVIEWER_MODEL = "claude-sonnet-4-6"
MAX_TOKENS_GEO = 8192
MAX_TOKENS_BRAND = 8192
MAX_TOKENS_CLUSTER = 8192
MAX_TOKENS_ENHANCER = 16000
MAX_TOKENS_TEACHER_REVIEW = 4096

# --- Parallelism ---
MAX_CONCURRENT_ARTICLES = 5       # asyncio semaphore limit
MAX_CONCURRENT_ENHANCE = 3        # asyncio semaphore limit for enhancement calls
MAX_CONCURRENT_TEACHER_REVIEW = 3  # asyncio semaphore limit for teacher review calls

# --- GEO Composite Weights (must sum to 1.0) ---
GEO_WEIGHTS = {
    "ai_citability": 0.25,
    "eeat": 0.20,
    "platform_optimization": 0.20,
    "brand_voice": 0.15,
    "seo_structure": 0.10,
    "schema_recommendations": 0.10,
}

# --- API ---
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# --- Google Sheets ---
GOOGLE_SERVICE_ACCOUNT_JSON = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "")
GOOGLE_SHEET_NAME = os.environ.get("GOOGLE_SHEET_NAME", "Wayground Content Evaluation - Batch 2")
GOOGLE_SHEET_ID = os.environ.get("GOOGLE_SHEET_ID", "")  # If set, open by ID instead of creating new
GDRIVE_ENHANCED_FOLDER_ID = os.environ.get("GDRIVE_ENHANCED_FOLDER_ID", "")  # Auto-set after first enhance run
GDRIVE_ENHANCED_FOLDER_NAME = os.environ.get("GDRIVE_ENHANCED_FOLDER_NAME", "Wayground Content - AEO Updated - Batch 2")
SHARE_EMAIL = os.environ.get("SHARE_EMAIL", "chandan@quizizz.com")

# --- Webflow ---
WEBFLOW_API_TOKEN = os.environ.get("WEBFLOW_API_TOKEN", "")
WEBFLOW_SITE_ID = os.environ.get("WEBFLOW_SITE_ID", "")
WEBFLOW_COLLECTIONS = {
    "Differentiated Learning": os.environ.get("WEBFLOW_COLLECTION_DIFFERENTIATED_LEARNING", ""),
    "Scaffolding": os.environ.get("WEBFLOW_COLLECTION_SCAFFOLDING", ""),
    "Engagement": os.environ.get("WEBFLOW_COLLECTION_ENGAGEMENT", ""),
}

# --- Retry ---
MAX_RETRIES = 3
RETRY_BASE_DELAY = 2.0  # seconds, doubles each retry
