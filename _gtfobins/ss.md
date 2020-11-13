---
description: |
  The read file content is limited to the first line and corrupted by an error message.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        ss -a -F $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./ss -a -F $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo ss -a -F $LFILE
---
