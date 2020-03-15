---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        base32 "$LFILE" | base32 --decode
  suid:
    - code: |
        LFILE=file_to_read
        base32 "$LFILE" | base32 --decode
  sudo:
    - code: |
        LFILE=file_to_read
        sudo base32 "$LFILE" | base32 --decode
---
