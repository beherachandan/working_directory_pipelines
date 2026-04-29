#!/bin/bash
# Rubric self-update cron — runs 2nd Monday of each month (after ground truth check)
# Rotates through topics from the 22-keyword queue
# Pass --topic as env var or hardcode for scheduled rotation

TOPIC="${CALIBRATION_TOPIC:-spaced repetition}"
cd /home/ec2-user/.openclaw/workspace/skills/geo-query/scripts
python3 rubric_self_update.py --topic "$TOPIC"
