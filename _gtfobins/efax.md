---
description: The content is actually parsed by the command, thus it may not be suitable for reading arbitrary files.
functions:
  suid:
    - code: |
        LFILE=file_to_read
        ./efax -d "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo efax -d "$LFILE"
---
