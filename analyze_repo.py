#!/usr/bin/env python3

import tarfile
import os
import subprocess

def main():
    os.chdir('/workspace')
    
    print("=== CSF Backup Repository Analysis ===")
    
    # Check tar file
    print("\n1. Analyzing tar file...")
    tar_empty = True
    try:
        if os.path.exists('csf.tgz'):
            with tarfile.open('csf.tgz', 'r:gz') as tar:
                members = tar.getmembers()
                if members:
                    tar_empty = False
                    print(f"Found {len(members)} items in tar file:")
                    for member in members[:10]:  # Show first 10
                        print(f"  {member.name}")
                    if len(members) > 10:
                        print(f"  ... and {len(members) - 10} more")
                    
                    print("Extracting...")
                    tar.extractall('.')
                else:
                    print("Tar file is empty")
        else:
            print("No tar file found")
    except Exception as e:
        print(f"Tar file error: {e}")
    
    # Check git
    print("\n2. Analyzing git repository...")
    git_has_files = False
    try:
        result = subprocess.run(['git', 'ls-files'], capture_output=True, text=True, check=True)
        if result.stdout.strip():
            git_has_files = True
            files = result.stdout.strip().split('\n')
            print(f"Git tracks {len(files)} files:")
            for f in files[:5]:
                print(f"  {f}")
            if len(files) > 5:
                print(f"  ... and {len(files) - 5} more")
            
            # Checkout files
            subprocess.run(['git', 'checkout', 'HEAD', '--', '.'], check=True)
            print("Files checked out from git")
        else:
            print("Git repository has no tracked files")
    except subprocess.CalledProcessError:
        print("Git operations failed or not a git repository")
    except Exception as e:
        print(f"Git error: {e}")
    
    # Final assessment
    print("\n3. Repository status...")
    source_files = []
    for root, dirs, files in os.walk('.'):
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            if (file.endswith(('.py', '.pl', '.sh', '.js')) and 
                not file.startswith(('recover_', 'check_', 'debug_', 'extract_', 'list_', 'test_', 'simple_', 'full_', 'git_', 'run_', 'show_', 'complete_'))):
                source_files.append(os.path.join(root, file))
    
    if source_files:
        print(f"Found {len(source_files)} source files:")
        for f in sorted(source_files):
            print(f"  {f}")
        return True
    else:
        print("No application source files found")
        if not tar_empty or git_has_files:
            print("Repository might need manual inspection")
        else:
            print("Repository appears to be empty - will create new implementation")
        return False

if __name__ == "__main__":
    has_source = main()
    
    if not has_source:
        print("\n=== Creating new CSF backup tool implementation ===")
        print("Since no existing source was found, I'll create a new implementation")
        print("that supports the '/q help' command as requested.")
