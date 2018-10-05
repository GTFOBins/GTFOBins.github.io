---
description: It can only append data if the destination exists.
functions:
  file-write:
    - code: |
        LFILE=file_to_write
        echo DATA | ./tee -a "$LFILE"
  suid:
    - code: |
        LFILE=file_to_write
        echo DATA | ./tee -a "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_write
        echo DATA | sudo tee -a "$LFILE"
---
