---
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo sort -m "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./sort -m "$LFILE"
  file-read:
    - code: |
        LFILE=file_to_read
        sort -m "$LFILE"
---
