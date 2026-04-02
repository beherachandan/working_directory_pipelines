"""YouTube Data API v3 wrappers for yt_pin_mvp."""

from googleapiclient.errors import HttpError


def list_playlists(youtube) -> list[dict]:
    """Return all playlists owned by the authenticated user."""
    results = []
    request = youtube.playlists().list(
        part="snippet,contentDetails",
        mine=True,
        maxResults=50,
    )
    while request:
        resp = request.execute()
        for item in resp.get("items", []):
            results.append({
                "id": item["id"],
                "title": item["snippet"]["title"],
                "thumbnail": item["snippet"]["thumbnails"].get("medium", {}).get("url", ""),
                "video_count": item["contentDetails"]["itemCount"],
            })
        request = youtube.playlists().list_next(request, resp)
    return results


def list_playlist_videos(youtube, playlist_id: str) -> list[dict]:
    """Return all videos in a playlist."""
    results = []
    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlist_id,
        maxResults=50,
    )
    while request:
        resp = request.execute()
        for item in resp.get("items", []):
            vid_id = item["contentDetails"]["videoId"]
            snippet = item["snippet"]
            results.append({
                "video_id": vid_id,
                "title": snippet["title"],
                "thumbnail": snippet["thumbnails"].get("medium", {}).get("url", ""),
            })
        request = youtube.playlistItems().list_next(request, resp)
    return results


def post_and_pin_comment(youtube, video_id: str, text: str) -> str:
    """Post a top-level comment and immediately pin it. Returns comment_thread_id."""
    # Step 1: Post the comment
    post_resp = youtube.commentThreads().insert(
        part="snippet",
        body={
            "snippet": {
                "videoId": video_id,
                "topLevelComment": {
                    "snippet": {"textOriginal": text}
                },
            }
        },
    ).execute()

    thread_id = post_resp["id"]
    top_comment_id = post_resp["snippet"]["topLevelComment"]["id"]

    # Step 2: Pin it via commentThreads.update with isPinned=True
    youtube.commentThreads().update(
        part="snippet",
        body={
            "id": thread_id,
            "snippet": {
                "videoId": video_id,
                "topLevelComment": {
                    "id": top_comment_id,
                    "snippet": {
                        "textOriginal": text,
                        "isPinned": True,
                    },
                },
                "canReply": True,
                "isPublic": True,
            },
        },
    ).execute()

    return thread_id


def get_error_reason(e: HttpError) -> str:
    """Extract a human-readable error reason from an HttpError."""
    try:
        detail = e.error_details[0]
        reason = detail.get("reason", "unknown")
        message = detail.get("message", str(e))
        # Make common reasons friendlier
        friendly = {
            "commentsDisabled": "Comments are disabled on this video.",
            "forbidden": "You can only pin comments on your own channel's videos.",
            "videoNotFound": "Video not found.",
        }
        return friendly.get(reason, f"{reason}: {message}")
    except (IndexError, AttributeError, KeyError):
        return str(e)
