---
functions:
  file-read:
  - code: |
      LFILE=file_to_read
      tail -c1G "$LFILE"
  suid-enabled:
  - code: |
      LFILE=file_to_read
      ./tail -c1G "$LFILE"
  sudo-enabled:
  - code: |
      LFILE=file_to_read
      sudo tail -c1G "$LFILE"
---
