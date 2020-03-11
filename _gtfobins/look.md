---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        look '' "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./look '' "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo look '' "$LFILE"
---
