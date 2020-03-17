---
description: This only returns ASCII strings, thus it is not suitable for binary files.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        strings "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./strings "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo strings "$LFILE"
---
