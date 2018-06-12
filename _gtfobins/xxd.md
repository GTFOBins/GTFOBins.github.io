---
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo xxd "$LFILE" | xxd -r
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./xxd "$LFILE" | xxd -r
  file-read:
    - code: |
        LFILE=file_to_read
        xxd "$LFILE" | xxd -r
  file-write:
    - code: |
        LFILE=file_to_write
        echo data | xxd | xxd -r - "$LFILE"
---
