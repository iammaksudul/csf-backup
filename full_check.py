#!/usr/bin/env python3

import tarfile
import os
import subprocess

# Check if tar file exists and extract it
tar_path = '/workspace/csf.tgz'
if os.path.exists(tar_path):
    print(f"Tar file exists: {tar_path}")
    print(f"Size: {os.path.getsize(tar_path)} bytes")
    
    try:
        with tarfile.open(tar_path, 'r:gz') as tar:
            print("Tar file contents:")
            members = tar.getmembers()
            for member in members:
                print(f"  {member.name} ({'dir' if member.isdir() else 'file'}, {member.size} bytes)")
            
            if members:  # Only extract if there are members
                print("\nExtracting files...")
                tar.extractall('/workspace/')
                print("Extraction complete")
            else:
                print("Tar file is empty")
            
    except Exception as e:
        print(f"Error extracting tar file: {e}")
else:
    print("Tar file not found")

# Change to workspace directory
os.chdir('/workspace')

# Check git status
try:
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True, check=True)
    if result.stdout.strip():
        print(f"\nGit status shows changes:\n{result.stdout}")
    else:
        print("\nGit working directory is clean")
        
    # List files tracked by git
    result = subprocess.run(['git', 'ls-files'], capture_output=True, text=True, check=True)
    if result.stdout.strip():
        print(f"\nFiles tracked by git:\n{result.stdout}")
    else:
        print("\nNo files tracked by git")
        
except subprocess.CalledProcessError as e:
    print(f"Git command failed: {e}")

# List all files in workspace
print("\nAll files in workspace:")
for root, dirs, files in os.walk('/workspace'):
    # Skip .git directory for cleaner output
    if '.git' in dirs:
        dirs.remove('.git')
    
    level = root.replace('/workspace', '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        if not file.endswith('.py') or file in ['extract_and_list.py', 'debug_git.py', 'simple_git_check.py', 'list_all.py', 'list_tar.py', 'test_extract.py']:
            continue
        print(f'{subindent}{file}')

if __name__ == "__main__":
    pass