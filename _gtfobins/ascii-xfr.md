---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        ascii-xfr -ns "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./ascii-xfr -ns "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo ascii-xfr -ns "$LFILE"
---
