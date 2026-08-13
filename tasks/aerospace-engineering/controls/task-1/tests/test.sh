#!/bin/bash
set -e

mkdir -p /logs/verifier

score=$(python3 /tests/verify.py)

echo "Reward: $score"
echo "$score" > /logs/verifier/reward.txt