#!/bin/bash
cd /workspace

echo "=== Step 1: Checking and extracting tar file ==="
if [ -f "csf.tgz" ]; then
    echo "csf.tgz found, checking contents..."
    tar -tzf csf.tgz 2>/dev/null | head -10
    echo "Extracting..."
    tar -xzf csf.tgz 2>/dev/null
    echo "Extraction completed"
else
    echo "csf.tgz not found"
fi

echo -e "\n=== Step 2: Git repository recovery ==="
if [ -d ".git" ]; then
    echo "Git repository found, checking status..."
    git status --porcelain
    echo "Files tracked by git:"
    git ls-files
    echo "Checking out all files..."
    git checkout HEAD -- . 2>/dev/null
    echo "Checkout completed"
else
    echo "No git repository found"
fi

echo -e "\n=== Step 3: Final directory listing ==="
echo "All files in workspace:"
find . -type f -not -path './.git/*' | sort

echo -e "\n=== Step 4: Looking for main application files ==="
echo "Potential main files:"
find . -name "main*" -o -name "app*" -o -name "csf*" -o -name "backup*" -o -name "*.py" -o -name "*.pl" -o -name "*.sh" | grep -v -E '\./[a-z_]+\.py$' | sort