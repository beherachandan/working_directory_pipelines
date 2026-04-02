#!/usr/bin/env bash
# A/B test runner: fast (shard 0) → moderate (shard 1), fully sequential.
# Launch once and walk away:
#   nohup bash run_ab_test.sh > ab_logs/nohup_out.txt 2>&1 &
#   echo "PID: $!"
#
# Check progress any time:
#   tail -f ab_logs/ab_run_*.log
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="$SCRIPT_DIR/ab_logs"
mkdir -p "$LOG_DIR"

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="$LOG_DIR/ab_run_$TIMESTAMP.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

log "=== A/B Test Run: $TIMESTAMP ==="
log "Log file: $LOG_FILE"
log ""

# ── Fast run: shard 0, ~250–350 comments over 6h ─────────────────────────────
log "Starting FAST run (shard 0 of 2, mode=fast)..."
python "$SCRIPT_DIR/batch_scheduler.py" --mode fast --shard 0 --shards 2 \
    2>&1 | tee -a "$LOG_FILE"
log "FAST run complete."
log ""

# ── Moderate run: shard 1, ~100–130 comments over 15h ────────────────────────
log "Starting MODERATE run (shard 1 of 2, mode=moderate)..."
python "$SCRIPT_DIR/batch_scheduler.py" --mode moderate --shard 1 --shards 2 \
    2>&1 | tee -a "$LOG_FILE"
log "MODERATE run complete."
log ""

log "=== Both runs finished. Check batch_results_*.json for results. ==="
log "=== Tomorrow: python batch_scheduler.py --recheck  ==="
