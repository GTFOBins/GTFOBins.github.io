---
description: The output is actually an hex dump.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        hexdump -C "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./hexdump -C "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo hexdump -C "$LFILE"
---
