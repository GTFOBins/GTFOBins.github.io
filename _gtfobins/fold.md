---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        fold -w99999999 "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./fold -w99999999 "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo fold -w99999999 "$LFILE"
---
