---
description: |
  The file content is actually parsed so only a part of each line is returned as a part of an error message.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        ssh-keyscan -f $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./ssh-keyscan -f $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo ssh-keyscan -f $LFILE
---
