---
functions:
  file-write:
    - description: Write ASCII data to file.
      code: |
        LFILE=file_to_write
        echo "DATA" | iconv -o "$LFILE"
  file-read:
    - description: Read data from file as UTF-8.
      code: |
        LFILE=file_to_read
        iconv -f UTF8 "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./iconv -f UTF8 "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo iconv -f UTF8 "$LFILE"
---
