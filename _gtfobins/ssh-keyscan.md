---
description: |
  The read file content is corrupted by error prints.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        ssh-keyscan -f "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./ssh-keyscan -f "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo ssh-keyscan -f "$LFILE"
---
