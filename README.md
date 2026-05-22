# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1370**
- Today's entries: **2**
- Today's note: `notes/2026-05-23.md`

### Latest Entry

- Timestamp: `2026-05-23T06:36:33+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 69
- `Architecture`: 69
- `Backend`: 69
- `Code Quality`: 69
- `Databases`: 69

### Recent Timeline

- `2026-05-23T06:36:33+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-23T06:09:47+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-22T22:40:27+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-22T21:36:25+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-22T20:34:43+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-22T19:41:19+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-22T18:33:46+08:00` | **Log with stable keys** (Observability)
- `2026-05-22T17:26:19+08:00` | **Design for idempotency** (APIs)
- `2026-05-22T16:10:47+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-22T14:49:23+08:00` | **Rotate credentials on schedule** (Security)
