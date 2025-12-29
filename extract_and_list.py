import tarfile
import os

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
            
            print("\nExtracting files...")
            tar.extractall('/workspace/')
            print("Extraction complete")
            
    except Exception as e:
        print(f"Error extracting tar file: {e}")
else:
    print("Tar file not found")

# List all files in workspace after extraction
print("\nFiles in workspace after extraction:")
for root, dirs, files in os.walk('/workspace'):
    level = root.replace('/workspace', '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        if not file.startswith('.git'):
            print(f'{subindent}{file}')