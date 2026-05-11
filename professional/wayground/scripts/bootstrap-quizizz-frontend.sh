#!/usr/bin/env bash
# Bootstrap Quizizz frontend clone with pinned Node (see ../config/quizizz-frontend/.nvmrc).
# Usage: from anywhere — bash professional/wayground/scripts/bootstrap-quizizz-frontend.sh [path-to-repo-root]
set -euo pipefail
ROOT="${1:-$(cd "$(dirname "$0")/../_upstream/quizizz-frontend" && pwd)}"
export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
if [ ! -s "$NVM_DIR/nvm.sh" ]; then
  echo "nvm not found at $NVM_DIR/nvm.sh — install nvm first: https://github.com/nvm-sh/nvm"
  exit 1
fi
# shellcheck source=/dev/null
. "$NVM_DIR/nvm.sh"
cd "$ROOT"
[ -f .nvmrc ] || { echo "No .nvmrc in $ROOT — copy from professional/wayground/config/quizizz-frontend/.nvmrc"; exit 1; }
nvm install
nvm use
corepack enable
PNPM_VER=$(node -e "console.log(require('./package.json').packageManager.replace('pnpm@',''))")
corepack prepare "pnpm@${PNPM_VER}" --activate
pnpm install --no-frozen-lockfile
echo "Done. Run from repo root: pnpm run dev-admin"
