---
description: |
  `column` expects textual data.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        column $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./column $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo column $LFILE
---
