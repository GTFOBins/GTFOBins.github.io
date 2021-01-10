---
description: bitmap editor and converter utilities for the X Window System. Outputs the first line of the file to standard error (stderr).
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        atobm $LFILE 2>&1| awk -F"'" '{print $2}' | tr -d '\n'
  sudo:
    - code: |
        LFILE=file_to_read
        sudo atobm $LFILE 2>&1| awk -F"'" '{print $2}' | tr -d '\n'
  suid:
    - code: |
        LFILE=file_to_read
        ./atobm $LFILE 2>&1| awk -F"'" '{print $2}' | tr -d '\n'
---
