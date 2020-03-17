---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        highlight --no-doc --failsafe "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./highlight --no-doc --failsafe "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo highlight --no-doc --failsafe "$LFILE"
---
