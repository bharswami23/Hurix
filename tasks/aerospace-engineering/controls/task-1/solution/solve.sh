#!/bin/bash
set -e

mkdir -p /logs/agent

echo "=== solve.sh STARTED ==="

python3 /solution/solve.py
