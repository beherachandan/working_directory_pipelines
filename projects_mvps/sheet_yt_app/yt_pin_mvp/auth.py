"""OAuth 2.0 flow, token persistence, and session helpers for yt_pin_mvp."""

import os
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from itsdangerous import BadSignature, URLSafeTimedSerializer

SCOPES = [
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtube.force-ssl",
]


def _creds_dir() -> Path:
    return Path(os.environ["SHARED_CREDS_DIR"])


def _token_path() -> Path:
    return _creds_dir() / "token.json"


def _web_client_path() -> Path:
    return _creds_dir() / "web-oauth-client.json"


# ── OAuth flow ────────────────────────────────────────────────────────────────

def build_flow() -> Flow:
    return Flow.from_client_secrets_file(
        str(_web_client_path()),
        scopes=SCOPES,
        redirect_uri=os.environ["GOOGLE_REDIRECT_URI"],
    )


def get_authorization_url(flow: Flow) -> tuple[str, str]:
    url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true",
        prompt="consent",  # ensures refresh_token is always returned
    )
    return url, state


def exchange_code(flow: Flow, authorization_response: str) -> Credentials:
    flow.fetch_token(authorization_response=authorization_response)
    return flow.credentials


# ── Token persistence ─────────────────────────────────────────────────────────

def save_token(creds: Credentials) -> None:
    _token_path().write_text(creds.to_json())


def load_token() -> Credentials | None:
    path = _token_path()
    if not path.exists():
        return None
    creds = Credentials.from_authorized_user_file(str(path), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        save_token(creds)
    return creds if creds.valid else None


# ── YouTube service ───────────────────────────────────────────────────────────

def build_youtube_service(creds: Credentials):
    return build("youtube", "v3", credentials=creds)


# ── Session cookie helpers ────────────────────────────────────────────────────

_signer: URLSafeTimedSerializer | None = None


def _get_signer() -> URLSafeTimedSerializer:
    global _signer
    if _signer is None:
        _signer = URLSafeTimedSerializer(os.environ["SECRET_KEY"])
    return _signer


def create_session_cookie(data: dict) -> str:
    return _get_signer().dumps(data)


def read_session_cookie(cookie_value: str, max_age: int = 86400 * 7) -> dict | None:
    try:
        return _get_signer().loads(cookie_value, max_age=max_age)
    except BadSignature:
        return None
