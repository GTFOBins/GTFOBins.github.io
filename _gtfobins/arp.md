---
description: |
  The read file content is corrupted by error prints.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        arp -v -f "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./arp -v -f "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo arp -v -f "$LFILE"
---
