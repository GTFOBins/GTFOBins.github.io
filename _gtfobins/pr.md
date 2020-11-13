---
description: |
  The read file content is corrupted by additional output.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        pr $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        pr $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        pr $LFILE
---
