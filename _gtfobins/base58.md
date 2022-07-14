---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        base58 "$LFILE" | base58 --decode
  sudo:
    - code: |
        LFILE=file_to_read
        sudo base58 "$LFILE" | base58 --decode
---
