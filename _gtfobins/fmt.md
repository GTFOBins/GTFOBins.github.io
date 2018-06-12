---
description: |
  The read file content is not binary-safe.
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo fmt -pNON_EXISTING_PREFIX "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./fmt -pNON_EXISTING_PREFIX "$LFILE"
  file-read:
    - code: |
        LFILE=file_to_read
        fmt -pNON_EXISTING_PREFIX "$LFILE"
---
