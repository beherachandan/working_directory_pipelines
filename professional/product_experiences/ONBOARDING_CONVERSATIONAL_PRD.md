# PRD: US teacher conversational onboarding (A/B)

## Summary

Replace the linear **org → subject/grade → questions** onboarding stack with an optional **guided, conversational first step** for **US teachers only**, controlled by a **multivariate feature flag**. Control keeps today’s flow unchanged.

## Goals

- **Primary:** Improve time-to-first-relevant resource during onboarding without lowering profile completion quality.
- **Secondary:** Increase engagement with search-driven discovery during onboarding.
- **Non-goals (v1):** Full LLM chat; replacing ES/org-picker backend services.

## Audience & eligibility

| Layer | Rule |
|--------|------|
| **Product** | Teacher persona (`user.isTeacher`), United States (`requestCountry === 'US'`). |
| **Experiment** | Feature flag variant `conversational`; all others see **control**. |

Occupation is reflected in `isTeacher` after role selection; country uses existing **`requestCountry`** (same surface area as other onboarding logic).

## Experiment design

| Variant | Key | UX |
|---------|-----|-----|
| **A — Control** | `control` (default) | Current components in the post-auth modal: `orgPicker` → `subjectGradePicker` → `onboardingQuestions` (subject to existing guards). User stays on `/admin` (or current route). |
| **B — Treatment** | `conversational` | After post-auth, redirect to **`/admin/onb_exp_1`** — a dedicated full-page experience (`onb-exp-1` route) hosting `ConversationalOnboardingFlow`: intent capture, optional refine (subject/grade pills), **search v2** previews (`getPublicQuizzesV3` with `/search/v2/public`), optional **school/org** (`OrgPickerRevamp`). On completion, marks onboarding complete and navigates back to `/admin`. |

### Routing

- **Route:** `name: onb-exp-1`, `path: /admin/onb_exp_1`, `meta.layout: 'auth'` (focused, no admin shell). Registered in `packages/onboarding/src/routes.ts`.
- **Redirect logic:** `useOnboardingComposable()` checks the flag + eligibility on mount. Treatment users are pushed to `/admin/onb_exp_1` (and the legacy modal does **not** render). Control users see the unchanged modal flow.
- **No-loop guard:** Redirect only fires when `route.path !== '/admin/onb_exp_1'` and `shouldShow` is true; the page calls `markOnboardingComplete` on finish so subsequent navigations bypass the gate.

### Backend configuration (required before prod)

Register flag key:

`onboarding-conversational-us-2026`

- **Type:** Multivariate string (or equivalent).
- **Values:** `control` | `conversational`.
- **Default:** `control` when absent (safe fallback in code).

Forced overrides via existing Feature Flags service / cookies continue to work (`shared-services/FeatureFlagsService`).

## User journey (Treatment)

1. **Intro + intent:** Named assistant copy (“Mira”), example chips, free-text intent.
2. **Refine (optional):** “Refine details” syncs heuristics from `extractIntentSlots` and shows subject + grade pills; “Continue” persists `subject_tags` + `grades` via `UserAPIService.updateInfo` (same contract as `SubjectGradeSelector`).
3. **Search preview (optional):** “Show resources (top picks)” calls `getPublicQuizzesV3` with `size: 2`, `use-search-service-v2-be` (URL `/search/v2/public` when enforced), filters from collected slots. “+ More results” routes to `admin-search-all-term` with the current query. “Continue setup” moves on.
4. **Org:** If legacy rules would have shown org picker, render `OrgPickerRevamp` (ES-backed flows unchanged). Otherwise emit to the next step.
5. **Questions:** Existing `onboardingQuestions` step for non-SND users, unchanged.

## Analytics (recommended events)

Already emitted in v1 implementation:

- `onboarding_conversational_refine_clicked`
- `onboarding_conversational_show_resources`
- Reuses `WebEvents.ADD_SUBJECTS_GRADES` with `source: post-authentication-onboarding-conversational`

Add in dashboard:

- Funnel: modal shown → refine → search clicked → subject/grade saved → org completed → onboarding complete.
- Variant dimension from flag value.

## Success metrics

- TTFR proxy: click on search preview or “Open in search” within session.
- Profile completion: `subject_tags`, `grades`, org attach rate vs control.
- Drop-off at each onboarding step (modal analytics).

## Risks & mitigations

| Risk | Mitigation |
|------|------------|
| Flag misconfigured | Default `control`; code gates US + teacher. |
| Search latency | Loading state + non-blocking continue. |
| Slot extraction wrong | Refine pills + manual overrides. |

## Engineering implementation map (quizizz/frontend)

> Implementation lives under `packages/onboarding/` in the **Quizizz frontend** monorepo (not this doc-only repo). Copy the changed files into your working branch there.

| Area | Location |
|------|----------|
| Flag + cohort | `onboardingComposable.ts` — `isConversationalOnboardingTreatment()` |
| Treatment redirect | `onboardingComposable.ts` — `onMounted` early-exits to `ONBOARDING_EXPERIMENT_PATH` |
| Treatment page | `components/onboarding-pages/onb_exp_1/index.vue` (calls `ConversationalOnboardingFlow`, then `markOnboardingComplete` + `window.location = '/admin'`) |
| Treatment route | `routes.ts` — `name: onb-exp-1`, `path: /admin/onb_exp_1` |
| Control stack | `getOnboardingComponents()` (orgPicker, subjectGradePicker, onboardingQuestions) |
| Conversational UI | `components/PostAuthenticationOnboarding/ConversationalOnboardingFlow.vue` |
| Intent heuristics | `utils/conversationalIntentSlots.ts` |
| Constants | `constants/onboardingExperiment.constants.ts`, `constants/orgPickerCountries.constants.ts` |
| Dependency | `package.json` peer `search` workspace |

## Rollout

1. Register **`onboarding-conversational-us-2026`** in Feature Flags service with default **`control`**.
2. Internal QA: force `conversational` via cookie / forced flag tooling.
3. Ramp percentage of US teachers; monitor errors and funnel.
4. Iterate on NLU (optional second phase: server-side qualifiers `/v3/qualifiers` already exists in SearchService).

## Open follow-ups

- Wire **content type** (quiz vs lesson) into filters when product taxonomy is fixed.
- Localized subject detection beyond keyword map.
- Deeper A/A validation on analytics schema.
