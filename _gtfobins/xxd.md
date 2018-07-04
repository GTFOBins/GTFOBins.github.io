---
functions:
  file-write:
  - code: |
      LFILE=file_to_write
      echo data | xxd | xxd -r - "$LFILE"
  file-read:
  - code: |
      LFILE=file_to_read
      xxd "$LFILE" | xxd -r
  suid-enabled:
  - code: |
      LFILE=file_to_read
      ./xxd "$LFILE" | xxd -r
  sudo-enabled:
  - code: |
      LFILE=file_to_read
      sudo xxd "$LFILE" | xxd -r
---
