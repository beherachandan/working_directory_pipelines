"""Atomic progress tracking — read/write progress.json safely."""
import json
import os
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path


@dataclass
class ProgressState:
    done: list[str] = field(default_factory=list)
    failed: dict[str, str] = field(default_factory=dict)   # item_num → error message
    pending: list[str] = field(default_factory=list)
    cluster_done: list[str] = field(default_factory=list)  # e.g. "Scaffolding/Core"
    started_at: str = ""
    last_updated: str = ""


def load_progress(progress_file: Path, all_item_nums: list[str]) -> ProgressState:
    """
    Load existing progress or create a fresh state.
    Ensures every item in all_item_nums appears in done, failed, or pending.
    """
    if progress_file.exists():
        with open(progress_file) as f:
            data = json.load(f)
        state = ProgressState(
            done=data.get("done", []),
            failed=data.get("failed", {}),
            pending=data.get("pending", []),
            cluster_done=data.get("cluster_done", []),
            started_at=data.get("started_at", ""),
            last_updated=data.get("last_updated", ""),
        )
        # Add any new items not already tracked
        accounted = set(state.done) | set(state.failed.keys()) | set(state.pending)
        for item_num in all_item_nums:
            if item_num not in accounted:
                state.pending.append(item_num)
    else:
        state = ProgressState(
            pending=list(all_item_nums),
            started_at=_now(),
        )

    return state


def save_progress(state: ProgressState, progress_file: Path) -> None:
    """Atomic write via temp file + rename."""
    state.last_updated = _now()
    tmp = progress_file.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(asdict(state), f, indent=2)
    os.replace(tmp, progress_file)


def mark_done(item_num: str, state: ProgressState) -> None:
    if item_num in state.pending:
        state.pending.remove(item_num)
    if item_num in state.failed:
        del state.failed[item_num]
    if item_num not in state.done:
        state.done.append(item_num)


def mark_failed(item_num: str, error: str, state: ProgressState) -> None:
    if item_num in state.pending:
        state.pending.remove(item_num)
    if item_num in state.done:
        state.done.remove(item_num)
    state.failed[item_num] = error


def mark_cluster_done(cluster_key: str, state: ProgressState) -> None:
    """cluster_key format: 'Scaffolding' or 'Scaffolding/Core'"""
    if cluster_key not in state.cluster_done:
        state.cluster_done.append(cluster_key)


def save_article_result(result: dict, articles_dir: Path, item_num: str, slug: str) -> None:
    """Save article evaluation result as JSON."""
    articles_dir.mkdir(parents=True, exist_ok=True)
    safe_slug = slug.replace("/", "-")[:60]
    path = articles_dir / f"{item_num}-{safe_slug}.json"
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(result, f, indent=2)
    os.replace(tmp, path)


def load_article_result(articles_dir: Path, item_num: str) -> dict | None:
    """Load an article result JSON. Returns None if not found."""
    for path in articles_dir.glob(f"{item_num}-*.json"):
        with open(path) as f:
            return json.load(f)
    return None


def load_all_article_results(articles_dir: Path, item_nums: list[str]) -> list[dict]:
    """Load all completed article results for the given item numbers."""
    results = []
    for item_num in item_nums:
        r = load_article_result(articles_dir, item_num)
        if r:
            results.append(r)
    return results


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
