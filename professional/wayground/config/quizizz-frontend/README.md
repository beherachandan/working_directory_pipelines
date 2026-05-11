# Quizizz frontend — pinned toolchain (template)

Copy these files into the root of your **`quizizz/frontend`** clone (same folder as that repo’s `package.json`):

- **`.nvmrc`** — Node version (must match `engines.node` in the monorepo `package.json`).

Then from that directory:

```bash
# nvm (https://github.com/nvm-sh/nvm)
export NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
nvm install
nvm use

# pnpm version from package.json "packageManager" (e.g. pnpm@10.27.0)
corepack enable
corepack prepare pnpm@10.27.0 --activate

pnpm install
pnpm run dev-admin
```

**Alternatives to nvm:** [fnm](https://github.com/Schniz/fnm), [mise](https://mise.jdx.dev/), [Volta](https://volta.sh/) — all can read `.nvmrc` or a `mise.toml` you add yourself.

For end-to-end onboarding + the conversational flag, see `knowledge/LOCAL_FRONTEND_DEV.md` in this repo.
