---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        msgconv -P $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        msgconv -P $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        msgconv -P $LFILE
---
