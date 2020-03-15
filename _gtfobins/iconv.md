---
functions:
  file-write:
    - description: Write ASCII data to file.
      code: |
        LFILE=file_to_write
        echo "DATA" | inconv -o "$LFILE"
  file-read:
    - description: Read data from file as UTF-8.
      code: |
        LFILE=file_to_read
        inconv -f UTF8 "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./inconv -f UTF8 "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo inconv -f UTF8 "$LFILE"
---
