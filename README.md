# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1493**
- Today's entries: **2**
- Today's note: `notes/2026-06-01.md`

### Latest Entry

- Timestamp: `2026-06-01T06:36:25+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 75
- `Architecture`: 75
- `Backend`: 75
- `Code Quality`: 75
- `Databases`: 75

### Recent Timeline

- `2026-06-01T06:36:25+08:00` | **Retry only safe operations** (Networking)
- `2026-06-01T06:08:27+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-31T21:57:22+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-31T21:12:16+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-31T20:34:30+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-31T19:49:34+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-31T19:10:28+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-31T18:27:21+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-31T17:32:01+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-31T16:20:51+08:00` | **Log with stable keys** (Observability)
