# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **130**
- Today's entries: **17**
- Today's note: `notes/2026-04-22.md`

### Latest Entry

- Timestamp: `2026-04-22T17:31:32+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 7
- `Architecture`: 7
- `Backend`: 7
- `Code Quality`: 7
- `Databases`: 7

### Recent Timeline

- `2026-04-22T17:31:32+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-22T16:33:39+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-22T15:33:13+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-22T14:36:22+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-22T13:45:30+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-22T12:56:24+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-22T11:02:58+08:00` | **Log with stable keys** (Observability)
- `2026-04-22T09:33:36+08:00` | **Design for idempotency** (APIs)
- `2026-04-22T08:20:57+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-22T07:13:36+08:00` | **Rotate credentials on schedule** (Security)
