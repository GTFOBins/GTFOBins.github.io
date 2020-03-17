---
description: The output is actually an hex dump.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        hd "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./hd "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo hd "$LFILE"
---
