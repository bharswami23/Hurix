#!/bin/bash
set -e

mkdir -p /logs/agent/
#cp /solution/results.xlsx /logs/agent/results.xlsx

echo "=== solve.sh STARTED ==="

echo "Looking for oracle_results.xlsx..."
find / -name "oracle_results.xlsx" 2>/dev/null

python3 /solution/solve.py