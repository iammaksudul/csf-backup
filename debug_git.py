import subprocess
import os

os.chdir('/workspace')

# Check git status
print("=== Git Status ===")
result = subprocess.run(['git', 'status'], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)

# List files in commit
print("\n=== Files in HEAD commit ===")
result = subprocess.run(['git', 'ls-tree', '-r', 'HEAD'], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)

# Check current directory
print("\n=== Current directory contents ===")
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(result.stdout)

# Try to checkout files
print("\n=== Checking out files ===")
result = subprocess.run(['git', 'checkout', 'HEAD', '--', '.'], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)

# Check directory again
print("\n=== Directory after checkout ===")
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(result.stdout)