# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2850**
- Today's entries: **20**
- Today's note: `notes/2026-08-26.md`

### Latest Entry

- Timestamp: `2026-08-26T22:26:29+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 143
- `Architecture`: 143
- `Backend`: 143
- `Code Quality`: 143
- `Databases`: 143

### Recent Timeline

- `2026-08-26T22:26:29+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-26T21:34:00+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-26T20:17:42+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-26T19:44:39+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-26T19:01:06+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-26T18:18:11+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-26T17:40:41+08:00` | **Log with stable keys** (Observability)
- `2026-08-26T16:54:14+08:00` | **Design for idempotency** (APIs)
- `2026-08-26T15:59:13+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-26T15:01:33+08:00` | **Rotate credentials on schedule** (Security)
