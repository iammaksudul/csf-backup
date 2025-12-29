#!/bin/bash
cd /workspace

echo "=== Checking tar file ==="
if [ -f "csf.tgz" ]; then
    echo "csf.tgz exists"
    echo "Size: $(stat -c%s csf.tgz) bytes"
    echo "Contents:"
    tar -tzf csf.tgz 2>/dev/null || echo "Error reading tar file or empty"
else
    echo "csf.tgz not found"
fi

echo -e "\n=== Git repository check ==="
if [ -d ".git" ]; then
    echo "Git repository found"
    echo "Current branch: $(git branch --show-current 2>/dev/null || echo 'unknown')"
    echo "Files tracked by git:"
    git ls-files 2>/dev/null || echo "No files tracked"
    echo "Git status:"
    git status --porcelain 2>/dev/null || echo "Git status failed"
else
    echo "Not a git repository"
fi

echo -e "\n=== Directory listing ==="
ls -la

echo -e "\n=== Looking for source files ==="
find . -name "*.py" -o -name "*.sh" -o -name "*.js" -o -name "*.pl" -o -name "*.rb" | grep -v "^./\." | head -20