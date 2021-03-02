---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        gzip -f $LFILE  -t
  suid:
    - code: |
        LFILE=file_to_read
        gzip -f $LFILE  -t
  sudo:
    - code: |
        LFILE=file_to_read
        gzip -f $LFILE  -t
---
