"""
Fetch YouTube transcripts for research project.
Uses youtube-transcript-api (free, no API key required).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import (
        NoTranscriptFound,
        TranscriptsDisabled,
        VideoUnavailable,
    )
except ImportError:
    print("Install: pip install youtube-transcript-api")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "research" / "youtube-transcripts"

VIDEOS = [
    {
        "slug": "kevin-indig-google-will-kill-your-traffic",
        "video_id": "jQXvbeYF5go",
        "title": "Google Will Kill Your Traffic - Here's How You Adapt | Kevin Indig",
        "author": "Kevin Indig",
        "published": "2025",
        "url": "https://www.youtube.com/watch?v=jQXvbeYF5go",
    },
    {
        "slug": "ryan-law-how-to-win-in-ai-search",
        "video_id": "mL1W1SMtTT4",
        "title": "How to Win in AI Search (Real Data, No Hype) | Ryan Law",
        "author": "Ryan Law",
        "published": "2025",
        "url": "https://www.youtube.com/watch?v=mL1W1SMtTT4",
    },
    {
        "slug": "lily-ray-future-of-seo",
        "video_id": "z0LOeXXFB8U",
        "title": "The Future of SEO with Lily Ray",
        "author": "Lily Ray",
        "published": "2024",
        "url": "https://www.youtube.com/watch?v=z0LOeXXFB8U",
    },
    {
        "slug": "michal-suski-optimize-content-with-surfer",
        "video_id": "HsAIXxvSzfQ",
        "title": "Surfer Academy: How to Optimize Content with Surfer",
        "author": "Michal Suski",
        "published": "2025-02-27",
        "url": "https://www.youtube.com/watch?v=HsAIXxvSzfQ",
    },
    {
        "slug": "patrick-stox-ai-search-strategy-geo",
        "video_id": "RwKKLnyXCig",
        "title": "Top SEO Experts Build Me an AI Search Strategy (GEO)",
        "author": "Patrick Stox",
        "published": "2026-01-21",
        "url": "https://www.youtube.com/watch?v=RwKKLnyXCig",
    },
    {
        "slug": "eli-schwartz-rethinking-seo-age-of-ai",
        "video_id": "Z71yGshPTwk",
        "title": "Rethinking SEO in the age of AI | Eli Schwartz",
        "author": "Eli Schwartz",
        "published": "2024-09-19",
        "url": "https://www.youtube.com/watch?v=Z71yGshPTwk",
    },
    {
        "slug": "aleyda-solis-ai-prompts-for-seo",
        "video_id": "WZL6mb3r2u4",
        "title": "Aleyda Solis' 6 Elements of Effective AI Prompts for SEO",
        "author": "Aleyda Solis",
        "published": "2024",
        "url": "https://www.youtube.com/watch?v=WZL6mb3r2u4",
    },
    {
        "slug": "kyle-roof-2024-2025-seo-strategy",
        "video_id": "1RggBJ4Fu9Y",
        "title": "Updating your 2024 & 2025 SEO Strategy with Kyle Roof",
        "author": "Kyle Roof",
        "published": "2024",
        "url": "https://www.youtube.com/watch?v=1RggBJ4Fu9Y",
    },
    {
        "slug": "sam-oh-chatgpt-rank-google",
        "video_id": "dHW-izBq2-I",
        "title": "I Used ChatGPT to Rank #1 in Google (in One Hour)",
        "author": "Sam Oh",
        "published": "2024-03-20",
        "url": "https://www.youtube.com/watch?v=dHW-izBq2-I",
    },
    {
        "slug": "britney-muller-actionable-ai-for-marketers",
        "video_id": "i9oShrzRzNA",
        "title": "Actionable AI for Marketers – The Human in the Loop",
        "author": "Britney Muller",
        "published": "2025",
        "url": "https://www.youtube.com/watch?v=i9oShrzRzNA",
    },
]


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def fetch_one(video: dict) -> dict:
    video_id = video["video_id"]
    author_dir = OUTPUT_DIR / slugify(video["author"])
    author_dir.mkdir(parents=True, exist_ok=True)
    out_path = author_dir / f"{video['slug']}.md"

    try:
        fetched = YouTubeTranscriptApi().fetch(
            video_id, languages=["en", "en-US", "en-GB"]
        )
    except (NoTranscriptFound, TranscriptsDisabled, VideoUnavailable) as exc:
        return {"video_id": video_id, "status": "error", "message": str(exc)}
    except Exception as exc:  # noqa: BLE001 — log any network/API failure per video
        return {"video_id": video_id, "status": "error", "message": str(exc)}

    lines = []
    for item in fetched:
        start = int(item.start)
        minutes, seconds = divmod(start, 60)
        timestamp = f"{minutes:02d}:{seconds:02d}"
        lines.append(f"[{timestamp}] {item.text}")

    body = "\n".join(lines)
    markdown = f"""# {video['title']}

- **Author:** {video['author']}
- **Published:** {video['published']}
- **URL:** {video['url']}
- **Video ID:** `{video_id}`
- **Fetched via:** `youtube-transcript-api` (Python)

---

## Transcript

{body}
"""
    out_path.write_text(markdown, encoding="utf-8")
    meta_path = author_dir / f"{video['slug']}.meta.json"
    meta_path.write_text(json.dumps(video, indent=2), encoding="utf-8")

    return {
        "video_id": video_id,
        "status": "ok",
        "path": str(out_path.relative_to(ROOT)),
        "segments": len(fetched),
    }


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results = [fetch_one(v) for v in VIDEOS]
    summary_path = OUTPUT_DIR / "fetch-log.json"
    summary_path.write_text(json.dumps(results, indent=2), encoding="utf-8")

    ok = sum(1 for r in results if r["status"] == "ok")
    print(f"Fetched {ok}/{len(results)} transcripts -> {OUTPUT_DIR}")
    for r in results:
        if r["status"] != "ok":
            print(f"  FAIL {r['video_id']}: {r['message']}")


if __name__ == "__main__":
    main()
