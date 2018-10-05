---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        unexpand -t99999999 "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./unexpand -t99999999 "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo unexpand -t99999999 "$LFILE"
---
