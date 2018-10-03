---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        grep '' $LFILE
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./grep '' $LFILE
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo grep '' $LFILE
---
