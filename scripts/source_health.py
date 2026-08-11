"""Bounded, concurrent health checks for canonical paper URLs."""

from __future__ import annotations

import concurrent.futures
import socket
import urllib.error
import urllib.request
from typing import Any, Callable, Dict, Optional, Sequence


USER_AGENT = "super-library-source-audit/0.4 (+https://github.com/asimfish/super_library)"


def classify_http_status(status: int) -> str:
    """Classify a response without treating access controls as broken links."""
    if 200 <= status < 400:
        return "reachable"
    if status in {401, 403, 405, 429, 451}:
        return "blocked"
    if status in {404, 410}:
        return "broken"
    if 500 <= status < 600:
        return "transient"
    return "unexpected"


def check_url(source: Dict[str, Any], timeout: float) -> Dict[str, Any]:
    """Fetch only enough of a URL to resolve redirects and obtain a status."""
    request = urllib.request.Request(
        source["url"],
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/pdf;q=0.9,*/*;q=0.1",
            "Range": "bytes=0-0",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status = int(response.getcode())
            response.read(1)
            return {
                "source_id": source["id"],
                "url": source["url"],
                "final_url": response.geturl(),
                "http_status": status,
                "status": classify_http_status(status),
                "detail": "",
            }
    except urllib.error.HTTPError as exc:
        return {
            "source_id": source["id"],
            "url": source["url"],
            "final_url": exc.geturl(),
            "http_status": int(exc.code),
            "status": classify_http_status(int(exc.code)),
            "detail": str(exc.reason or "HTTP error"),
        }
    except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
        reason = getattr(exc, "reason", exc)
        return {
            "source_id": source["id"],
            "url": source["url"],
            "final_url": None,
            "http_status": None,
            "status": "transient",
            "detail": str(reason),
        }
    except Exception as exc:  # Defensive boundary for SSL and redirect edge cases.
        return {
            "source_id": source["id"],
            "url": source["url"],
            "final_url": None,
            "http_status": None,
            "status": "unexpected",
            "detail": f"{type(exc).__name__}: {exc}",
        }


def verify_sources(
    sources: Sequence[Dict[str, Any]],
    *,
    timeout: float = 15.0,
    workers: int = 12,
    checker: Optional[Callable[[Dict[str, Any], float], Dict[str, Any]]] = None,
) -> Sequence[Dict[str, Any]]:
    """Check sources concurrently and return stable source-ID order."""
    check = checker or check_url
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(check, source, timeout): source["id"]
            for source in sources
        }
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    return sorted(results, key=lambda item: item["source_id"])


def health_summary(results: Sequence[Dict[str, Any]]) -> Dict[str, int]:
    counts: Dict[str, int] = {"total": len(results)}
    for result in results:
        status = result["status"]
        counts[status] = counts.get(status, 0) + 1
    return counts
