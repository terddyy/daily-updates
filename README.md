# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1070**
- Today's entries: **298**
- Today's note: `notes/2026-05-02.md`

### Latest Entry

- Timestamp: `2026-05-02T08:43:03+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 54
- `Architecture`: 54
- `Backend`: 54
- `Code Quality`: 54
- `Databases`: 54

### Recent Timeline

- `2026-05-02T08:43:03+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-02T08:43:02+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-02T08:43:01+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-02T08:43:00+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-02T08:42:59+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-02T08:42:58+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-02T08:42:57+08:00` | **Log with stable keys** (Observability)
- `2026-05-02T08:42:56+08:00` | **Design for idempotency** (APIs)
- `2026-05-02T08:42:55+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-02T08:42:54+08:00` | **Rotate credentials on schedule** (Security)
