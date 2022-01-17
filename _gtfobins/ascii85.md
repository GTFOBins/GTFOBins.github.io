---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        ascii85 "$LFILE" | ascii85 --decode
  sudo:
    - code: |
        LFILE=file_to_read
        sudo ascii85 "$LFILE" | ascii85 --decode
---
