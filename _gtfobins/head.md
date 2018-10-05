---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        head -c1G "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./head -c1G "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo head -c1G "$LFILE"
---
