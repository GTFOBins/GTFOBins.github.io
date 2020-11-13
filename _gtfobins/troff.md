---
description: |
  The read file content is corrupted by error prints.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        troff $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./troff $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo troff $LFILE
---
