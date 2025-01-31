---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        sort -m "$LFILE"
  file-write:
    - code: |
        LFILE=file_to_write
        echo DATA | sort -o "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./sort -m "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo sort -m "$LFILE"
---
