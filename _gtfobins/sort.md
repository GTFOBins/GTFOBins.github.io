---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        sort -m "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./sort -m "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo sort -m "$LFILE"
---
