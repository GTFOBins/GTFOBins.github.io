---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        cut -d "" -f1 "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./cut -d "" -f1 "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo cut -d "" -f1 "$LFILE"
---
