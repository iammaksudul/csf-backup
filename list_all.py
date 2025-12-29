import os

print("All files and directories in /workspace:")
for item in os.listdir('/workspace'):
    path = os.path.join('/workspace', item)
    if os.path.isdir(path):
        print(f"DIR:  {item}")
        # List contents of directories
        try:
            for subitem in os.listdir(path):
                print(f"  {subitem}")
        except PermissionError:
            print("  (permission denied)")
    else:
        print(f"FILE: {item}")