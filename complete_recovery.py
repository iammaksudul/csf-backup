import tarfile
import os
import subprocess

os.chdir('/workspace')

print("=== Checking tar file contents ===")
try:
    with tarfile.open('csf.tgz', 'r:gz') as tar:
        members = tar.getmembers()
        print(f"Tar file contains {len(members)} items:")
        for member in members:
            print(f"  {member.name} ({'dir' if member.isdir() else 'file'}, {member.size} bytes)")
        
        if members:
            print("\nExtracting files...")
            tar.extractall('.')
            print("Extraction complete")
        else:
            print("Tar file is empty")
            
except Exception as e:
    print(f"Error with tar file: {e}")

print("\n=== Checking git repository ===")
try:
    # Check what files git knows about
    result = subprocess.run(['git', 'ls-files'], capture_output=True, text=True)
    if result.returncode == 0 and result.stdout.strip():
        print("Files tracked by git:")
        for line in result.stdout.strip().split('\n'):
            print(f"  {line}")
        
        # Check if files exist in working directory
        print("\nChecking if tracked files exist:")
        for filename in result.stdout.strip().split('\n'):
            if filename.strip():
                exists = os.path.exists(filename)
                print(f"  {filename}: {'EXISTS' if exists else 'MISSING'}")
        
        # Try to checkout files
        print("\nChecking out files from git...")
        checkout_result = subprocess.run(['git', 'checkout', 'HEAD', '--', '.'], capture_output=True, text=True)
        if checkout_result.returncode == 0:
            print("Checkout successful")
        else:
            print(f"Checkout failed: {checkout_result.stderr}")
    else:
        print("No files tracked by git or git command failed")
        
except Exception as e:
    print(f"Git operations failed: {e}")

print("\n=== Final file listing ===")
all_files = []
for root, dirs, files in os.walk('.'):
    if '.git' in dirs:
        dirs.remove('.git')
    for file in files:
        if not file.endswith(('.py', '.sh')) or file.startswith(('recover_', 'check_', 'debug_', 'extract_', 'list_', 'test_', 'simple_', 'full_', 'git_', 'run_', 'show_')):
            continue
        filepath = os.path.join(root, file)
        all_files.append(filepath)

if all_files:
    print("Source files found:")
    for f in sorted(all_files):
        print(f"  {f}")
else:
    print("No source files found - repository might be empty or need initialization")