---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        efax -d "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./efax -d "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo efax -d "$LFILE"
---
