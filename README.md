# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1350**
- Today's entries: **13**
- Today's note: `notes/2026-05-21.md`

### Latest Entry

- Timestamp: `2026-05-21T20:23:50+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 68
- `Architecture`: 68
- `Backend`: 68
- `Code Quality`: 68
- `Databases`: 68

### Recent Timeline

- `2026-05-21T20:23:50+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-21T19:08:59+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-21T17:48:02+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-21T16:16:14+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-21T14:54:34+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-21T13:29:44+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-21T11:47:40+08:00` | **Log with stable keys** (Observability)
- `2026-05-21T10:23:26+08:00` | **Design for idempotency** (APIs)
- `2026-05-21T09:22:11+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-21T08:14:15+08:00` | **Rotate credentials on schedule** (Security)
