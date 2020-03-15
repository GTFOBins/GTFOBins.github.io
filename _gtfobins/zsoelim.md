---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        zsoelim "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        zsoelim "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo zsoelim "$LFILE"
---
