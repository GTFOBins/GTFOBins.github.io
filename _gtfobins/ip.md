---
description: |
  The read file content is corrupted by error prints.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        ip -force -batch "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./ip -force -batch "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo ip -force -batch "$LFILE"
---
