---
description: |
  The file content is actually parsed so only a part of the first line is returned as a part of an error message.
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
