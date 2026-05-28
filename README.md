# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1450**
- Today's entries: **11**
- Today's note: `notes/2026-05-28.md`

### Latest Entry

- Timestamp: `2026-05-28T17:33:23+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 73
- `Architecture`: 73
- `Backend`: 73
- `Code Quality`: 73
- `Databases`: 73

### Recent Timeline

- `2026-05-28T17:33:23+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-28T16:08:22+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-28T14:31:58+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-28T12:59:01+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-28T11:27:12+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-28T10:00:37+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-28T09:12:29+08:00` | **Log with stable keys** (Observability)
- `2026-05-28T08:08:16+08:00` | **Design for idempotency** (APIs)
- `2026-05-28T07:30:58+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-28T06:49:35+08:00` | **Rotate credentials on schedule** (Security)
