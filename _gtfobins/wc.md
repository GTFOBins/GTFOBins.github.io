---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        wc --f "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./wc --f "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo wc --f "$LFILE"
---
