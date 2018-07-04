---
functions:
  file-read:
  - code: |
      LFILE=file_to_read
      unexpand -t99999999 "$LFILE"
  suid-enabled:
  - code: |
      LFILE=file_to_read
      ./unexpand -t99999999 "$LFILE"
  sudo-enabled:
  - code: |
      LFILE=file_to_read
      sudo unexpand -t99999999 "$LFILE"
---
