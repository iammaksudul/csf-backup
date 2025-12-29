import tarfile

# List contents of the tar file
with tarfile.open('/workspace/csf.tgz', 'r:gz') as tar:
    print("Contents of csf.tgz:")
    for member in tar.getmembers():
        print(f"  {member.name} ({'dir' if member.isdir() else 'file'})")