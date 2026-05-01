# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **353**
- Today's entries: **81**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:04:48+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 18
- `Architecture`: 18
- `Backend`: 18
- `Code Quality`: 18
- `Databases`: 18

### Recent Timeline

- `2026-05-01T09:04:48+08:00` | **Retry only safe operations** (Networking)
- `2026-05-01T09:04:47+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-01T09:04:46+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-01T09:04:45+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-01T09:04:44+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-01T09:04:43+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-01T09:04:42+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-01T09:04:41+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-01T09:04:40+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-01T09:04:39+08:00` | **Log with stable keys** (Observability)
