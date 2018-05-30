---
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo cat "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./cat "$LFILE"
  file-read:
    - code: |
        LFILE=file_to_read
        cat "$LFILE"
---
