# Local frontend dev (Quizizz / Wayground monorepo)

Node does not have Python-style “virtual environments.” The usual pattern is:

1. **Pin the Node version** (this repo uses **20.19.3** — see `engines` in `package.json`).
2. **Pin the package manager** (`packageManager`: **pnpm@10.27.0**).
3. **Install once** into the monorepo’s `node_modules` (isolated per clone, not global site-packages).

The closest parallel to `python -m venv` is: **right Node + pnpm + `pnpm install` in the repo root**.

---

## 1. Version managers (pick one)

| Tool | Notes |
|------|--------|
| **nvm** | Most common on macOS. After install, your shell should load `~/.nvm/nvm.sh` (see nvm install instructions). In the monorepo root, `nvm use` reads `.nvmrc`. |
| **fnm** / **mise** / **Volta** | Can also install/use Node 20.19.3; some read `.nvmrc` automatically. |

**Template `.nvmrc` (copy to `quizizz/frontend` root):** see `../config/quizizz-frontend/.nvmrc` in this workspace.

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
cd /path/to/quizizz-frontend
nvm install    # installs version from .nvmrc
nvm use
node -v        # should print v20.19.3
```

---

## 2. pnpm via Corepack (matches the monorepo)

```bash
corepack enable
corepack prepare pnpm@10.27.0 --activate
pnpm -v
```

If Corepack is unavailable, install pnpm globally with the same major version the repo expects.

---

## 3. Install and run the admin app (onboarding lives here)

From the **monorepo root**:

```bash
pnpm install
```

If you changed dependencies (e.g. added a workspace peer) and CI uses a frozen lockfile, refresh once:

```bash
pnpm install --no-frozen-lockfile
```

Or use the workspace helper (loads nvm + installs):

```bash
bash professional/wayground/scripts/bootstrap-quizizz-frontend.sh /path/to/quizizz-frontend
```

Then:

```bash
pnpm run dev-admin
```

Console prints which localhost port the admin app uses (often **3002**). Complete SSO/signup flow until post-auth onboarding appears.

---

## 4. Feature flags locally (`onboarding-conversational-us-2026`)

Flags are loaded by **`shared-services/FeatureFlagsService`**. For local overrides you can:

### A. Browser console (fastest for one-off checks)

After the app loads (admin SPA):

```javascript
window.__featureFlags?.setForcedFeature('onboarding-conversational-us-2026', 'conversational');
location.reload();
```

To go back to control:

```javascript
window.__featureFlags?.setForcedFeature('onboarding-conversational-us-2026', 'control');
location.reload();
```

### B. Cookie `feature_flags` (persists across reloads)

The service reads JSON from the **`feature_flags`** cookie. Example shape (adjust domain/path for your dev host):

```javascript
document.cookie =
  'feature_flags=' +
  encodeURIComponent(
    JSON.stringify({ 'onboarding-conversational-us-2026': 'conversational' }),
  ) +
  '; path=/';
location.reload();
```

### C. Staging / dev API

If your environment loads flags from the Feature Flags service, configure the deployment so **`onboarding-conversational-us-2026`** returns `conversational` for your test user or cohort — same as production wiring, without console hacks.

---

## 5. Eligibility for the conversational onboarding path

Client-side gates (in addition to the flag):

- **`requestCountry === 'US'`** (server-derived country on `serverData`).
- **`user.isTeacher === true`**.

If you do not see the treatment, verify country + teacher state and that the flag value is exactly **`conversational`** (not `ENABLED`).

### Treatment URL

When the flag is `conversational` for an eligible user, the post-auth modal does **not** open. Instead the user is redirected to:

**`http://localhost:3002/admin/onb_exp_1`**

You can also visit it directly while testing. On completion, the page marks `bts.onboardingComplete = true` and navigates to `/admin` so the gate stops firing.

---

## 6. Optional: helper script in this workspace

You can keep a clone under `professional/wayground/_upstream/quizizz-frontend` (often gitignored) and run the same `nvm use` + `pnpm install` + `pnpm run dev-admin` from that path after copying `.nvmrc` into it.

---

## 7. Troubleshooting

**`injection "requestCountry" not found` on `LoginSignupModal`:** Parents must `provide('requestCountry')` and `provide('isMobile')`. **`explore-core`** (`SearchView.vue`) and **`search-core`** (`SRPLayout.vue`) now provide both from `useServerDataStore` + device bridge. The modal **`inject`s defaults** (`US`, `false`) if a route omits providers.

**`Failed to fetch dynamically imported module` / `@fs/.../LoginSignupModal.vue`:**

- Often a **stale Vite URL** from another folder or an old dev session (error paths like `checkfront-frontend` vs your real clone mean the browser is requesting modules **outside** the running server root).
- Fix: **stop** processes on port **3002**, restart **`pnpm run dev-admin`** from **this** monorepo root only, then **hard reload** (⌘⇧R) or disable cache in DevTools → Network.

---

## 8. PR checklist before production

- [ ] Commit **`.nvmrc`** at monorepo root (20.19.3) so CI and teammates match engines.
- [ ] Register **`onboarding-conversational-us-2026`** in the Feature Flags service with default **`control`**.
- [ ] Validate treatment on **US teacher** test accounts in a lower environment with the flag set to **`conversational`**.
- [ ] Confirm analytics events for the funnel (see `ONBOARDING_CONVERSATIONAL_PRD.md`).
