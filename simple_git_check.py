import subprocess
import os

os.chdir('/workspace')

try:
    # Get the commit hash
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True)
    commit_hash = result.stdout.strip()
    print(f"Current commit: {commit_hash}")
    
    # List files in the commit
    result = subprocess.run(['git', 'ls-tree', '-r', commit_hash], capture_output=True, text=True, check=True)
    print("Files in commit:")
    print(result.stdout)
    
    # Show the commit details
    result = subprocess.run(['git', 'show', '--name-only', commit_hash], capture_output=True, text=True, check=True)
    print("Commit details:")
    print(result.stdout)
    
except subprocess.CalledProcessError as e:
    print(f"Git command failed: {e}")
    print(f"stdout: {e.stdout}")
    print(f"stderr: {e.stderr}")