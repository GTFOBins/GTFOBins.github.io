---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        redcarpet "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./redcarpet "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo redcarpet "$LFILE"
---
