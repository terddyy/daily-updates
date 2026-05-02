# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **793**
- Today's entries: **21**
- Today's note: `notes/2026-05-02.md`

### Latest Entry

- Timestamp: `2026-05-02T08:38:26+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 40
- `Architecture`: 40
- `Backend`: 40
- `Code Quality`: 40
- `Databases`: 40

### Recent Timeline

- `2026-05-02T08:38:26+08:00` | **Retry only safe operations** (Networking)
- `2026-05-02T08:38:25+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-02T08:38:24+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-02T08:38:23+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-02T08:38:22+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-02T08:38:21+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-02T08:38:20+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-02T08:38:19+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-02T08:38:18+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-02T08:38:17+08:00` | **Log with stable keys** (Observability)
