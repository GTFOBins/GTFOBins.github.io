---
description: This can be run with elevated privileges to change permissions and then read, write, or execute a file.
functions:
  suid:
    - code: |
        LFILE=file_to_change
        ./chmod 0777 $LFILE
  sudo:
    - code: |
        LFILE=file_to_change
        sudo chmod 0777 $LFILE
---
