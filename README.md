# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2490**
- Today's entries: **3**
- Today's note: `notes/2026-08-12.md`

### Latest Entry

- Timestamp: `2026-08-12T07:17:07+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 125
- `Architecture`: 125
- `Backend`: 125
- `Code Quality`: 125
- `Databases`: 125

### Recent Timeline

- `2026-08-12T07:17:07+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-12T06:46:24+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-12T06:16:40+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-11T22:38:48+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-11T22:11:34+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-11T21:30:59+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-11T20:48:26+08:00` | **Log with stable keys** (Observability)
- `2026-08-11T20:24:00+08:00` | **Design for idempotency** (APIs)
- `2026-08-11T19:59:49+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-11T19:31:15+08:00` | **Rotate credentials on schedule** (Security)
