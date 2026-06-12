# Collection notes

## Tools used

| Tool | Purpose |
|------|---------|
| `youtube-transcript-api` (Python) | Pull captions from 10 practitioner videos |
| Cursor + Claude | Structure repo, draft annotations, run fetch script |
| Manual collection | LinkedIn posts (platform blocks automated scraping) |

## LinkedIn limitation

LinkedIn does not allow reliable public scraping without authentication. Per the assignment email ("scrape or manually collect"), posts in `/research/linkedin-posts/` were **copied manually** from public post URLs, webinar recaps, and cross-posted articles—with source links and dates.

If you need more posts per author, open their profile → filter recent posts → paste into the author file with date + URL.

## Transcript script

```bash
pip install -r requirements.txt
python scripts/fetch_transcripts.py
```

Output: `/research/youtube-transcripts/{author}/{slug}.md` and `fetch-log.json`.

## Quality bar

Skipped:

- Generic "10 AI SEO tools" listicle authors  
- Accounts that only reshare news without original tests  
- GEO influencers with no visible client or product work  

Prioritized:

- People who publish **data** (Ahrefs, Kevin Indig, Kyle Roof tests)  
- **B2B / SaaS** operators (Ryan Law, Eli Schwartz, Sam Oh)  
- **Tool builders** who eat their own cooking (Michal Suski / Surfer)
