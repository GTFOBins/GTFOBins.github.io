---
description: Utility to Secure Delete A File in Unix
functions:
  file-write:
    - code: |
        LFILE=file_to_delete
        shred -u $LFILE
  sudo:
    - code: |
        LFILE=file_to_delete
        sudo shred -u $LFILE
---
