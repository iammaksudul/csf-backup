import tarfile
import os

# Extract the tar file
with tarfile.open('/workspace/csf.tgz', 'r:gz') as tar:
    tar.extractall('/workspace/')
    
# List the contents
for root, dirs, files in os.walk('/workspace'):
    level = root.replace('/workspace', '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        if not file.startswith('.') and file != 'csf.tgz':
            print(f'{subindent}{file}')