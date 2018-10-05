---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        base64 "$LFILE" | base64 --decode
  suid:
    - code: |
        LFILE=file_to_read
        ./base64 "$LFILE" | base64 --decode
  sudo:
    - code: |
        LFILE=file_to_read
        sudo base64 "$LFILE" | base64 --decode
---
