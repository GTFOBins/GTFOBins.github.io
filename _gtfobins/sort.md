---
description: The read file content is corrupted by being sorted.
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo sort "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./sort "$LFILE"
  file-read:
    - code: |
        LFILE=file_to_read
        sort "$LFILE"
---
