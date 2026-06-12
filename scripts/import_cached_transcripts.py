"""Import transcripts from cached web fetches into research/youtube-transcripts/."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "youtube-transcripts"
AGENT = Path(
    r"C:\Users\saikr\.cursor\projects\c-Users-saikr-Downloads-junior-growth-marketing-specialist-main-junior-growth-marketing-specialist-main\agent-tools"
)

MAP = {
    "ryan-law/how-to-win-in-ai-search": (
        "f1ea2b95-3b66-4e4d-a3f4-d1df3347ed7e.txt",
        "Ryan Law",
        "mL1W1SMtTT4",
        "How to Win in AI Search (Real Data, No Hype) | Ryan Law",
        "2025-10-28",
        "https://www.youtube.com/watch?v=mL1W1SMtTT4",
    ),
    "britney-muller/actionable-ai-for-marketers": (
        "184b3772-9db3-4111-a92c-41f8a65b9423.txt",
        "Britney Muller",
        "i9oShrzRzNA",
        "Actionable AI for Marketers – The Human in the Loop",
        "2025-04-01",
        "https://www.youtube.com/watch?v=i9oShrzRzNA",
    ),
    "kevin-indig/google-will-kill-your-traffic": (
        "6f82fa92-dfd3-49ae-aec9-3149dd860739.txt",
        "Kevin Indig",
        "jQXvbeYF5go",
        "Google Will Kill Your Traffic - Here's How You Adapt",
        "2025",
        "https://www.youtube.com/watch?v=jQXvbeYF5go",
    ),
    "eli-schwartz/rethinking-seo-age-of-ai": (
        "a7e8ceb8-f8e7-4592-8b47-9bc7d2391920.txt",
        "Eli Schwartz",
        "Z71yGshPTwk",
        "Rethinking SEO in the age of AI | Eli Schwartz",
        "2024-09-19",
        "https://www.youtube.com/watch?v=Z71yGshPTwk",
    ),
    "aleyda-solis/ai-prompts-for-seo": (
        "177e6cae-a0d1-422a-b9fb-a990cfefb687.txt",
        "Aleyda Solis",
        "WZL6mb3r2u4",
        "Aleyda Solis' 6 Elements of Effective AI Prompts for SEO",
        "2024",
        "https://www.youtube.com/watch?v=WZL6mb3r2u4",
    ),
    "kyle-roof/2024-2025-seo-strategy": (
        "68ed7ba8-3a31-42da-8a94-890b34ef2124.txt",
        "Kyle Roof",
        "1RggBJ4Fu9Y",
        "Updating your 2024 & 2025 SEO Strategy with Kyle Roof",
        "2024",
        "https://www.youtube.com/watch?v=1RggBJ4Fu9Y",
    ),
}


def main() -> None:
    for rel, (fname, author, vid, title, pub, url) in MAP.items():
        src = AGENT / fname
        if not src.exists():
            print(f"missing {fname}")
            continue
        text = src.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"## Transcript\s*\n(.*)", text, re.S)
        body = match.group(1).strip() if match else text
        if len(body) > 100_000:
            body = (
                body[:100_000]
                + "\n\n---\n\n*[Truncated. Run `python scripts/fetch_transcripts.py` for full file.]*\n"
            )
        author_slug = author.lower().replace(" ", "-")
        dest_dir = OUT / author_slug
        dest_dir.mkdir(parents=True, exist_ok=True)
        slug = rel.split("/")[-1]
        md = f"""# {title}

- **Author:** {author}
- **Published:** {pub}
- **URL:** {url}
- **Video ID:** `{vid}`
- **Source:** YouTube auto-captions

---

## Transcript

{body}
"""
        (dest_dir / f"{slug}.md").write_text(md, encoding="utf-8")
        print(f"wrote {author_slug}/{slug}.md ({len(body)} chars)")


if __name__ == "__main__":
    main()
