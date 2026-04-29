#!/bin/bash
# Monthly ground truth check — runs 1st Monday of each month
cd /home/ec2-user/.openclaw/workspace/skills/geo-query/scripts
python3 ground_truth_check.py --platform chatgpt
