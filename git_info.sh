#!/bin/bash
cd /workspace

echo "=== Git commit info ==="
git log --oneline

echo -e "\n=== Files in the commit ==="
git show --name-only HEAD

echo -e "\n=== Tree structure ==="
git ls-tree -r HEAD

echo -e "\n=== Current working directory files ==="
ls -la