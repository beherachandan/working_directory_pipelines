"""Wayground YT Pin MVP — FastAPI application."""

import os

from dotenv import load_dotenv

load_dotenv()

# Required for local dev: allows OAuth over http://localhost
if os.environ.get("OAUTHLIB_INSECURE_TRANSPORT"):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

from fastapi import FastAPI, HTTPException, Request, Response  # noqa: E402
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse  # noqa: E402
from fastapi.templating import Jinja2Templates  # noqa: E402
from googleapiclient.errors import HttpError  # noqa: E402
from pydantic import BaseModel  # noqa: E402

from auth import (  # noqa: E402
    build_flow,
    build_youtube_service,
    create_session_cookie,
    exchange_code,
    get_authorization_url,
    load_token,
    read_session_cookie,
    save_token,
)
from youtube import (  # noqa: E402
    get_error_reason,
    list_playlist_videos,
    list_playlists,
    post_and_pin_comment,
)

app = FastAPI(title="Wayground YT Pin")
templates = Jinja2Templates(directory="templates")

SESSION_COOKIE = "wg_session"
STATE_COOKIE = "wg_oauth_state"


# ── Auth helpers ──────────────────────────────────────────────────────────────

def _get_session(request: Request) -> dict | None:
    val = request.cookies.get(SESSION_COOKIE)
    return read_session_cookie(val) if val else None


def _require_auth(request: Request):
    """Return valid Credentials or raise 401."""
    session = _get_session(request)
    if not session or not session.get("authenticated"):
        raise HTTPException(status_code=401, detail="Not authenticated")
    creds = load_token()
    if not creds:
        raise HTTPException(status_code=401, detail="Token missing or expired — please log in again")
    return creds


# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def landing(request: Request, error: str = None):
    if _get_session(request) and load_token():
        return RedirectResponse("/dashboard", status_code=302)
    return templates.TemplateResponse("landing.html", {"request": request, "error": error})


@app.get("/auth/login")
async def auth_login():
    flow = build_flow()
    url, state = get_authorization_url(flow)
    redirect = RedirectResponse(url, status_code=302)
    redirect.set_cookie(STATE_COOKIE, state, max_age=300, httponly=True, samesite="lax")
    return redirect


@app.get("/auth/callback")
async def auth_callback(request: Request, state: str = None, code: str = None, error: str = None):
    if error:
        return RedirectResponse(f"/?error={error}", status_code=302)
    stored_state = request.cookies.get(STATE_COOKIE)
    if not stored_state or stored_state != state:
        raise HTTPException(status_code=400, detail="State mismatch — possible CSRF attack")

    flow = build_flow()
    creds = exchange_code(flow, str(request.url))
    save_token(creds)

    redirect = RedirectResponse("/dashboard", status_code=302)
    redirect.set_cookie(
        SESSION_COOKIE,
        create_session_cookie({"authenticated": True}),
        max_age=86400 * 7,
        httponly=True,
        samesite="lax",
    )
    redirect.delete_cookie(STATE_COOKIE)
    return redirect


@app.get("/auth/logout")
async def auth_logout():
    redirect = RedirectResponse("/", status_code=302)
    redirect.delete_cookie(SESSION_COOKIE)
    return redirect


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    creds = _require_auth(request)
    youtube = build_youtube_service(creds)
    playlists = list_playlists(youtube)
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "playlists": playlists,
    })


@app.get("/api/playlist/{playlist_id}/videos")
async def get_videos(playlist_id: str, request: Request):
    creds = _require_auth(request)
    youtube = build_youtube_service(creds)
    videos = list_playlist_videos(youtube, playlist_id)
    return JSONResponse({"videos": videos})


class PinRequest(BaseModel):
    video_id: str
    comment_text: str


@app.post("/api/pin")
async def pin_comment(pin_req: PinRequest, request: Request):
    creds = _require_auth(request)
    youtube = build_youtube_service(creds)
    try:
        thread_id = post_and_pin_comment(youtube, pin_req.video_id, pin_req.comment_text)
        return JSONResponse({
            "success": True,
            "comment_thread_id": thread_id,
            "message": "Comment posted and pinned!",
        })
    except HttpError as e:
        return JSONResponse(
            {"success": False, "error": get_error_reason(e)},
            status_code=int(e.resp.status),
        )
