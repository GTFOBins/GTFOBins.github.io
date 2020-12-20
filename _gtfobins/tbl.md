---
description: |
  The read file content is corrupted by additional text at the beginning.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        tbl $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./tbl $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo tbl $LFILE
---
