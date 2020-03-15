---
description: |
  Each line is corrupted by a prefix string. Also consider that lines are actually parsed as `kickstart` scripts thus some file contents may lead to unexpected results.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        ksshell -i $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./ksshell -i $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo ksshell -i $LFILE
---
