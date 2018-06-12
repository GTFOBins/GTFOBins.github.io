---
description: |
  The read file content is corrupted by replacing tabs with spaces; not binary-safe.
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo expand "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./expand "$LFILE"
  file-read:
    - code: |
        LFILE=file_to_read
        expand "$LFILE"
---
