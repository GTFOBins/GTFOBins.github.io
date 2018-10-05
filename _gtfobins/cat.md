---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        cat "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./cat "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo cat "$LFILE"
---
