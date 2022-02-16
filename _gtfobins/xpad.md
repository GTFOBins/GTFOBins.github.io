---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        xpad -f "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo xpad -f "$LFILE"
---
