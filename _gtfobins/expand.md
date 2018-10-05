---
description: The read file content is corrupted by replacing tabs with spaces.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        expand "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./expand "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo expand "$LFILE"
---
