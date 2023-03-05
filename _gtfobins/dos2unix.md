---
functions:
  file-write:
    - code: |
        LFILE=file_to_write
        RFILE=file_to_read
        dos2unix -f -n "$RFILE" "$LIFE"
  file-read:
    - code: |
        LFILE=file_to_read
        dos2unix -f < "$LIFE"
---
