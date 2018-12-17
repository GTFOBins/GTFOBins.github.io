---
functions:
  file-write:
    - code: |
        LFILE=file_to_write
        echo DATA | openssl enc -out "$LFILE"
    - code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        openssl enc -in "$TF" -out "$LFILE"
  file-read:
    - code: |
        LFILE=file_to_read
        openssl enc -in "$LFILE"
  suid:
    - code: |
        LFILE=file_to_write
        echo DATA | openssl enc -out "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_write
        echo DATA | sudo openssl enc -out "$LFILE"
---
