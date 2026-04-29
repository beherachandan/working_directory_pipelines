#!/bin/bash
cd /home/ec2-user/.openclaw/workspace/skills/geo-query/scripts
python3 calibration.py \
  --topic "growth mindset" \
  --variations 4 \
  --runs 3 \
  --platforms chatgpt \
  --scores-file /home/ec2-user/.openclaw/workspace/memory/research/scoring-runs/d2-scores-corpus.json
