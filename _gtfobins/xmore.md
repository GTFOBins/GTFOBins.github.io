---
description: It allows privileged read of a file if it has a special file permission.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        xmore $LFILE
    - code: |
        LFILE=file_to_read
        xmore $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        xmore $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        xmore $LFILE 
---
