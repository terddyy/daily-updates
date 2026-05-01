# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **730**
- Today's entries: **458**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:11:05+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 37
- `Architecture`: 37
- `Backend`: 37
- `Code Quality`: 37
- `Databases`: 37

### Recent Timeline

- `2026-05-01T09:11:05+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-01T09:11:04+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-01T09:11:03+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-01T09:11:02+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-01T09:11:01+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-01T09:11:00+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-01T09:10:59+08:00` | **Log with stable keys** (Observability)
- `2026-05-01T09:10:58+08:00` | **Design for idempotency** (APIs)
- `2026-05-01T09:10:57+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-01T09:10:56+08:00` | **Rotate credentials on schedule** (Security)
