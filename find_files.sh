#!/bin/bash
cd /workspace
find . -type f -not -path './.git/*' -not -name '*.tgz' -not -name 'extract.sh' -not -name 'test_extract.py' -not -name 'list_tar.py' -not -name 'list_all.py' -not -name 'show_commit.sh' -not -name 'find_files.sh'