# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1650**
- Today's entries: **13**
- Today's note: `notes/2026-06-12.md`

### Latest Entry

- Timestamp: `2026-06-12T21:52:37+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 83
- `Architecture`: 83
- `Backend`: 83
- `Code Quality`: 83
- `Databases`: 83

### Recent Timeline

- `2026-06-12T21:52:37+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-12T20:44:13+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-12T19:30:27+08:00` | **Automate rollback paths** (DevOps)
- `2026-06-12T18:10:36+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-12T16:33:01+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-12T14:52:25+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-12T13:08:57+08:00` | **Log with stable keys** (Observability)
- `2026-06-12T11:26:03+08:00` | **Design for idempotency** (APIs)
- `2026-06-12T10:00:47+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-12T09:01:51+08:00` | **Rotate credentials on schedule** (Security)
