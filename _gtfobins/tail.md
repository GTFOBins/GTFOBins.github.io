---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        tail -c1G "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./tail -c1G "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo tail -c1G "$LFILE"
---
