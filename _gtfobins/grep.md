---
description: |
  There are many `grep` flavors that in many cases are just copies, symlinks or wrappers around the original binary that may share the same behavior, for example: `egrep`, `fgrep`, `zgrep`, etc.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        grep '' $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./grep '' $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo grep '' $LFILE
---
