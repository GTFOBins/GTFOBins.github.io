---
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo unexpand -t99999999 "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./unexpand -t99999999 "$LFILE"
  file-read:
    - code: |
        LFILE=file_to_read
        unexpand -t99999999 "$LFILE"
---
