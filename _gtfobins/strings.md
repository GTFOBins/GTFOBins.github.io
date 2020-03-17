---
description: Only strings are returned from the read file.
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
