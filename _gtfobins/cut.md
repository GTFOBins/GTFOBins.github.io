---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        cut -d "" -f1 "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./cut -d "" -f1 "$LFILE"
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo cut -d "" -f1 "$LFILE"
---
