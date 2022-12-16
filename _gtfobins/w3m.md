---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        w3m "$LFILE" -dump
  suid:
    - code: |
        LFILE=file_to_read
        ./w3m "$LFILE" -dump
  sudo:
    - code: |
        LFILE=file_to_read
        sudo w3m "$LFILE" -dump
---
