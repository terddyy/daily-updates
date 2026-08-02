# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2290**
- Today's entries: **3**
- Today's note: `notes/2026-08-02.md`

### Latest Entry

- Timestamp: `2026-08-02T16:58:55+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 115
- `Architecture`: 115
- `Backend`: 115
- `Code Quality`: 115
- `Databases`: 115

### Recent Timeline

- `2026-08-02T16:58:55+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-02T08:12:30+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-02T07:10:55+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-01T22:44:30+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-01T18:39:29+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-01T16:54:17+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-01T14:29:09+08:00` | **Log with stable keys** (Observability)
- `2026-08-01T11:49:55+08:00` | **Design for idempotency** (APIs)
- `2026-08-01T08:08:21+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-31T22:06:12+08:00` | **Rotate credentials on schedule** (Security)
