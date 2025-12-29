import os
import subprocess

os.chdir('/workspace')

# Check git objects to see what was committed
try:
    # Get the commit hash
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True)
    if result.returncode == 0:
        commit_hash = result.stdout.strip()
        print(f"Current commit: {commit_hash}")
        
        # Show what files are in this commit
        result2 = subprocess.run(['git', 'ls-tree', '-r', commit_hash], capture_output=True, text=True)
        if result2.returncode == 0:
            print("Files in the commit:")
            print(result2.stdout)
        else:
            print("No files in commit or error listing files")
            
        # Try to checkout the files
        result3 = subprocess.run(['git', 'checkout', '.'], capture_output=True, text=True)
        print(f"Checkout result: {result3.returncode}")
        if result3.stderr:
            print(f"Checkout stderr: {result3.stderr}")
            
    else:
        print("No valid git repository or no commits")
        print(f"Error: {result.stderr}")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

# Also try to list all files recursively
print("\nAll files in workspace (recursive):")
for root, dirs, files in os.walk('/workspace'):
    # Skip .git directory for cleaner output
    if '.git' in root:
        continue
    level = root.replace('/workspace', '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f"{subindent}{file}")