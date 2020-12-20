---
description: This can be run with elevated privileges to change permissions (`6` denotes the SUID bits) and then read, write, or execute a file.
functions:
  suid:
    - code: |
        LFILE=file_to_change
        ./chmod 6777 $LFILE
  sudo:
    - code: |
        LFILE=file_to_change
        sudo chmod 6777 $LFILE
---
