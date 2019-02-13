---
description: |
  The read file content is corrupted by error prints.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        mtr --raw -F "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo mtr --raw -F "$LFILE"
---
