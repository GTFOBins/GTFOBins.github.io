---
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo cut -d "" "$LFILE" -f1
  file-read:
    - code: |
        LFILE=file_to_read
        cut -d "" "$LFILE" -f1
---
