# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2650**
- Today's entries: **7**
- Today's note: `notes/2026-08-17.md`

### Latest Entry

- Timestamp: `2026-08-17T10:59:06+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 133
- `Architecture`: 133
- `Backend`: 133
- `Code Quality`: 133
- `Databases`: 133

### Recent Timeline

- `2026-08-17T10:59:06+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-17T09:48:35+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-17T07:58:39+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-17T07:44:18+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-17T07:19:04+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-17T06:50:53+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-17T06:29:38+08:00` | **Log with stable keys** (Observability)
- `2026-08-16T22:52:21+08:00` | **Design for idempotency** (APIs)
- `2026-08-16T22:39:01+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-16T22:24:13+08:00` | **Rotate credentials on schedule** (Security)
