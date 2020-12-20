---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        paste $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        paste $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo paste $LFILE
---
