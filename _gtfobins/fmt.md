---
description: The read file content is not binary-safe.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        fmt -pNON_EXISTING_PREFIX "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./fmt -pNON_EXISTING_PREFIX "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo fmt -pNON_EXISTING_PREFIX "$LFILE"
---
