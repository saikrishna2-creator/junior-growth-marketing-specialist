# Junior Growth Marketing Specialist — Portfolio Project

**Sai** · [100Hires](https://100hires.com) portfolio process  
**Repository:** [github.com/saikrishna2-creator/junior-growth-marketing-specialist](https://github.com/saikrishna2-creator/junior-growth-marketing-specialist)

---

## Step 1 — Environment setup ✓

See commit history for the original setup README (Cursor, Claude Code, Codex, GitHub).

---

## Step 2 — Research project

**Topic chosen:** [AI-powered SEO content production](#why-this-topic)

### Why this topic

Of the eight options, this one best matches the role and this assignment:

- The job is **daily AI-assisted content** with fact-checking and judgment—not volume for its own sake.
- B2B SaaS (100Hires) lives on **comparison pages, blogs, landing pages, and email**—all overlap with modern SEO/content.
- Strong **YouTube + LinkedIn** practitioner ecosystem → fits the API + manual collection workflow.
- Lets me show **technical execution** (transcript script) and **taste** (who is worth listening to).

I did not pick cold outreach or LinkedIn strategy alone—they are narrower. AI SEO sits at the intersection of content, data, and tools, which is where I want to work.

### What I collected

| Asset | Location |
|-------|----------|
| 10 experts + annotations | [`research/sources.md`](research/sources.md) |
| LinkedIn posts (manual) | [`research/linkedin-posts/`](research/linkedin-posts/) |
| YouTube transcripts (API) | [`research/youtube-transcripts/`](research/youtube-transcripts/) |
| Supporting articles | [`research/other/`](research/other/) |
| Transcript fetch script | [`scripts/fetch_transcripts.py`](scripts/fetch_transcripts.py) |

### Experts — why these 10

I optimized for **operators and researchers**, not the first Google result for "AI SEO tips."

| Expert | One-line reason |
|--------|-----------------|
| Kevin Indig | Original AI Overview / clickstream research; advised Shopify, Ramp |
| Ryan Law | Ahrefs citation studies; B2B content lead |
| Lily Ray | Algorithm + AEO recovery; calls out GEO spam |
| Michal Suski | Built Surfer; teaches production AI content workflows |
| Patrick Stox | Ahrefs AI search / Brand Radar research |
| Eli Schwartz | Product-led SEO for B2B (Zendesk, Gusto, WordPress) |
| Aleyda Solis | AI prompt frameworks + client-side SEO tests |
| Kyle Roof | 400+ SEO experiments; "bad SEO faster" warning |
| Sam Oh | Hands-on AI + snippet experiments at Ahrefs |
| Britney Muller | ML + SEO; human-in-the-loop AI education |

Full links, dates, and notes: [`research/sources.md`](research/sources.md).

### How I collected it

1. **YouTube transcripts** — Python script using `youtube-transcript-api` (free, no API key). One markdown file per video under `/research/youtube-transcripts/{author}/`.
2. **LinkedIn** — Manual copy from public posts (LinkedIn blocks reliable scraping). Organized by author in `/research/linkedin-posts/`.
3. **Other** — Blog posts and webinar recaps that add context for a future playbook.

Run the transcript fetch locally:

```bash
pip install -r requirements.txt
python scripts/fetch_transcripts.py
```

### Early themes (playbook-ready)

1. AI drafts are raw material—edit, verify, add information gain (Law, Muller, Roof).
2. Freshness and third-party mentions matter for AI citations (Law, Indig).
3. YouTube + transcripts are both input to LLMs and output in AI answers (Stox, Ray, Law).
4. Mid-funnel / product-led content wins as LLMs absorb top-of-funnel (Schwartz).
5. Workflows (templates, QA, dual optimization) beat one-shot prompts (Suski, Solis).

---

## Repository structure

```
research/
  sources.md
  linkedin-posts/     # one file per expert
  youtube-transcripts/
  other/
scripts/
  fetch_transcripts.py
requirements.txt
README.md
```

---

## Links

- Portfolio: [myjobportfolio.lovable.app](https://myjobportfolio.lovable.app)
