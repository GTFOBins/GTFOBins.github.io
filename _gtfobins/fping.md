---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        fping -f $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo fping -f $LFILE
---
