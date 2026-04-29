#!/bin/bash
cd /home/ec2-user/.openclaw/workspace/skills/geo-query/scripts
python3 calibration.py --topic "retrieval practice" --variations 4 --runs 3 --platforms chatgpt
