---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        head -c1G "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./head -c1G "$LFILE"
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo head -c1G "$LFILE"
---
