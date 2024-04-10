---
description: The result is displayed in a TUI interface.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        links "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./links "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo links "$LFILE"
---
