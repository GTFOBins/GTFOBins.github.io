---
description: |
  Each line is corrupted by a prefix string and wrapped inside single quotes.

functions:
  file-read:
    - code: |
        LFILE=file_to_read
        readelf -a @$LFILE
  suid:
    - code: |
        LFILE=file_to_read
        readelf -a @$LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo readelf -a @$LFILE
---
