# Quizizz / Wayground frontend — knowledge base

Canonical internal doc for product and engineering context when working on Wayground (Quizizz rebrand; public overview: [Quizizz becomes Wayground](https://wayground.com/home/from-quizizz-to-wayground)). **Legal entity remains Quizizz Inc.;** this repo is the **Quizizz** frontend monoreup.

**Upstream:** [https://github.com/quizizz/frontend](https://github.com/quizizz/frontend)  
**Note:** The GitHub **web UI and unauthenticated API** may return 404; the repository is still clonable over `git` for authorized users.

---

## Local dev (Node, pnpm, feature flags)

See **[LOCAL_FRONTEND_DEV.md](./LOCAL_FRONTEND_DEV.md)** — pin Node **20.19.3** (`.nvmrc`), **pnpm** via Corepack, run **`pnpm run dev-admin`**, and force **`onboarding-conversational-us-2026`** in the browser for conversational onboarding.

Pinned `.nvmrc` template: `../config/quizizz-frontend/.nvmrc`

---

## How to refresh this document (do this when touching frontend work)

1. Update the local mirror (see [Local upstream clone](#local-upstream-clone)):  
   `cd professional/wayground/_upstream/quizizz-frontend && git pull origin HEAD && git rev-parse HEAD && git log -1 --format='%ci %s'`
2. Re-skim `apps/admin/src/pages.ts` (feature route registration) and `packages/services/package.json` (`exports` = API client surfaces).
3. Append a row to [Scan log](#scan-log) with date, commit, and one-line summary of what changed in the doc.

---

## Scan log

| Date (UTC)   | Commit     | Notes |
|-------------|------------|--------|
| 2026-05-04  | `f0750f31` | Initial import: monorepo map, apps, packages, admin router composition, services exports, nuxt-ssr pages, dev ports. |

---

## Monorepo tooling

| Item | Value |
|------|--------|
| Orchestration | **TurboRepo** (`turbo.json`) |
| Package manager | **pnpm** `10.27.0` (workspace: `apps/*`, `packages/*`) |
| Node | **20.19.3** (see root `package.json` `engines`) |
| Core UI | **Vue 3** + **Vite**; **Nuxt 3** for SSR/SSG apps |
| TypeScript | Yes; shared `typescript-config` package |
| Lint | **oxlint** (`oxlint-config`); **ESLint** mentioned in README |
| Commits | **Commitizen** (repo badge / README) |

**Root scripts (selected):** `pnpm run dev` (all projects), `pnpm run dev-admin` (admin only), `turbo build` / `turbo build-dev`, per-app `dev-join`, `dev-practice`, `dev-search-ssr`, `build:admin`, `build:join`, `build:practice`, `test:ci` (vitest).

**Vite modes (from README):** `devenv`, `localenv`, `development` for different base URLs / environments.

---

## Applications (`apps/`)

Deployable or dev entrypoints. Package name = folder name unless noted.

| App | Role (PM summary) | Default dev port (where set in Vite) |
|-----|-------------------|--------------------------------------|
| **admin** | Primary **teacher / author** Vue SPA: hosts most product areas via composed routes. | **3002** |
| **join** | **Student / live session** join flow (live game entry). | **3001** |
| **practice** | **Practice** mode experience. | **3003** |
| **nuxt-ssr** | **SSR Nuxt** app: SEO/marketing-style routes (`pages/`), auth-ssg, resource library surface, print, LTI, generators, etc. | Nuxt default (typically 3000) |
| **search-ssr** | **Search**-oriented SSR (run via `pnpm run dev-search-ssr`). | **3008** (`nuxt dev --port 3008` in `package.json`) |
| **resource-library-app** | **Resource library** app shell (port **3007** in vite config; may overlap with differentiation-mvp in docs—verify when running). | **3007** |
| **future-teacher** | Future/variant teacher experience (prototype). | — |
| **mathverse-editor** | Mathverse editor. | — |
| **ai-extension** | **AI extension** (e.g. browser) dev on **3000** in vite config—avoid port clash with nuxt. | **3000** |
| **differentiation-mvp** | Differentiation MVP shell. | **3007** (same as resource-library in config; not all run at once) |

**README caveat:** `admin` default URL `http://localhost:3002` when using `dev-admin`.

---

## Admin app: how features attach

File: `apps/admin/src/pages.ts`. The admin router **aggregates route arrays** imported from feature packages (each package can expose `routes`). Examples of composed domains:

`onboarding`, `auth-shared`, `search`, `search-core`, `explore`, `explore-core`, `my-library`, `resource-library`, `classes`, `courses`, `activities`, `activity-dashboards`, `editor`, `lesson-editor`, `reports`, `org-dashboard`, `district-dashboard`, `differentiation`, `integrations`, `lti`, `pricing`, `sales-and-subscription`, `sales-and-subscription-new`, `ai`, `ai-workflows`, `content-moderation`, `growth`, `marketing`, `passage`, `interactive-video`, `qfw`, `qfw-landing`, `qdash`, `way-arena`, `wfb-ai-roleplay`, `impact-kits`, `worksheets`, `super-format-mvp`, `gcaddon`, `google-slides-addon`, `memes`, `shoutouts`, `generator-forms`, `sphagetti` (+ referrals), and more.

**Implication for PMs:** A “surface” (e.g. resource library, search, billing) is usually a **package** with routes consumed by **admin** and sometimes **nuxt-ssr** or another app.

---

## `packages/services` — typed API client surfaces

The `services` package exposes **feature-aligned HTTP/API modules** (built with Vite). Current `exports` include:

`users`, `library`, `classes`, `contentModeration`, `paidOrgLibrary`, `integrations`, `reports`, `sales-and-subscriptions`, `onboarding`, `activity`, `common-assessments`, `growth`, `organization`, `usageAnalytics`, `analytics`.

These align with backend capabilities; pair with `network-layer` and `shared-services` / `shared-domains` for requests and domain types.

---

## Feature packages (selected, by product theme)

Full list: ~90+ packages under `packages/`. Groupings for UX/service thinking:

| Theme | Packages (representative) |
|-------|---------------------------|
| **Authentication & session** | `auth-shared`, `auth-ssg`, `join-shared` |
| **Onboarding** | `onboarding`, `onboarding-modal` |
| **Search & discovery** | `search`, `search-core`, `explore`, `explore-core`, `category-pages` |
| **Library & content** | `my-library`, `resource-library`, `library-limits`, `lesson-editor`, `editor`, `editor-shared`, `generator-pages`, `generator-forms` |
| **Classes & instruction** | `classes`, `courses`, `activities`, `activity-dashboards`, `activity-dashboards-shared`, `lesson-dashboards`, `common-assessment`, `common-new-game-settings` |
| **Differentiation & accessibility** | `differentiation`, `differentiation-shared` |
| **Live game / practice** | `join-shared`, `practice-shared`; apps `join`, `practice` |
| **Reporting & analytics** | `reports`, `reports-shared`, `qdash`, `q-analytics`, `analytics-client`, `analytics-sdk` |
| **Org & district** | `org-dashboard`, `district-dashboard` |
| **Billing & pricing** | `sales-and-subscription`, `sales-and-subscription-new`, `pricing` |
| **AI** | `ai`, `ai-workflows`, `wfb-ai-roleplay`, `way-arena` |
| **Integrations** | `integrations`, `lti`, `gcaddon`, `google-slides-addon` |
| **Trust & safety** | `content-moderation` |
| **Marketing & growth** | `marketing`, `growth`, `qfw-landing`, `qfw`, `qfw-paywall` |
| **Shared UI & platform** | `shared-components`, `shared-layouts`, `shared-library`, `shared-icons`, `shell-layout`, `quizizz-ui`, `network-layer`, `translations-client`, `user-profile`, `user-settings`, `user-profile-settings` |

---

## Nuxt SSR (`apps/nuxt-ssr/pages`) — notable routes

Illustrative file-based routes (not exhaustive):

- `login.vue`, `signup/index.vue`, `signup/occupation.vue`
- `resource-library/index.vue`, `resource-library/[slug].vue`
- `library/[...slug].vue`
- `generators/index.vue`, `generators/[slug].vue`
- `print/[type]/[id].vue`
- `lti/auth/pending.vue`
- `admin/oauth/consent.vue`
- `admin/[quizType]/[id]/[[slug]].vue`

Use these for **SEO**, **shared links**, **LTI**, **print**, and **auth-related** entry flows vs the heavy **admin** SPA.

---

## Wayground / PM framing (public product story)

- Rebrand positions the product as **broader than quizzes**: supplemental curriculum, resources, **AI as assistive** (accommodations, generation hub), **standards alignment**, **lesson bundles**, programs such as **VoyageMath** (check current marketing for freshness).
- **Accounts, classes, resources, and integrations** largely continuous through rebrand; **wayground.com** replaces quizizz.com for teacher-facing surfaces over time.

---

## Local upstream clone

Path in this workspace: `professional/wayground/_upstream/quizizz-frontend` (gitignored to avoid committing vendor-scale trees).

```bash
git clone --depth 1 https://github.com/quizizz/frontend.git professional/wayground/_upstream/quizizz-frontend
```

---

## Related workspace paths

- Publishing / content automation: `projects_mvps/automating_publishing_webflow/` (often references Wayground marketing and editorial rules).

---

## Development lifecycle from this workspace (two-repo model)

`checking_claude` and `quizizz/frontend` are **separate Git repositories**. The clone under `professional/wayground/_upstream/quizizz-frontend` is **ignored by this workspace’s git** on purpose, so you **do not** mix frontend diffs into `checking_claude` commits. Work the frontend like any standalone repo: `cd` there, branch, stage, commit, push.

### Commit only what you intend

1. **Never** run `git add -A` at the monorepo root unless you mean it; you will pick up lockfile churn, generated assets, and unrelated packages.
2. **Stage by path** (explicit list of files or directories you touched):
   - `git add packages/foo/src/Bar.vue packages/foo/package.json`
3. **Stage hunks interactively** (best when a file has both wanted and experimental edits):
   - `git add -p path/to/file.vue` — accept or skip each chunk.
4. **Unstage mistakes** before committing:
   - `git restore --staged <path>` or `git reset -p` to unstage selectively.
5. **Review the commit**:
   - `git diff --staged` must show only the story you want in one commit.

### Keep management seamless

| Concern | Practice |
|--------|----------|
| **One feature = one branch** | From `main`/`develop` (follow team convention): `git checkout -b feat/short-name`. Merge via PR; keeps history reviewable. |
| **Small commits** | One logical change per commit (e.g. “fix search filter” not “fix search + bump dep + format”). |
| **Link project ↔ code** | In `checking_claude`, keep a one-line note (ticket ID, project folder, or link) in a local note or PR description—not a second copy of the code. |
| **Generated / local noise** | Do not commit `dist/`, `lib/`, `.turbo`, or env files; respect existing `.gitignore` in the frontend repo. |
| **Sync from upstream** | Before starting work: `git fetch && git rebase origin/<base>` (or merge) on your branch to reduce conflicts. |
| **Optional: patch out of this workspace** | If you prototype in a scratch folder here, `git diff` in the frontend clone is still the source of truth; you can `git apply` a saved patch, or copy only the listed files. |

### Cursor / IDE

Open the **frontend folder** as its own window or use the **Source Control** view scoped to that clone so status and commits apply to `quizizz/frontend`, not `checking_claude`.

---

## README gaps (root)

Root `README.md` still emphasizes **`admin`** only; the repo now contains **many apps and packages**. Treat this file and `apps/admin/src/pages.ts` as the **practical map** until README is expanded upstream.
