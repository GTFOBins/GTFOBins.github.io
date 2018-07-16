---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        fold -w99999999 "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./fold -w99999999 "$LFILE"
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo fold -w99999999 "$LFILE"
---
