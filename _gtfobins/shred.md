---
description: Utility to Secure Delete A File in Unix
functions:
  file-delete:
    - code: |
        LFILE=file_to_delete
        shred -u $LFILE
  sudo:
    - code: |
        LFILE=file_to_delete
        sudo shred -u $LFILE
---
