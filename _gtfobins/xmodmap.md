---
description: |
  The read file content is corrupted by error prints.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        xmodmap -v $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./xmodmap -v $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo xmodmap -v $LFILE
---
