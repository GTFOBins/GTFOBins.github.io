---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        cat "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./cat "$LFILE"
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo cat "$LFILE"
---
