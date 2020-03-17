---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        dialog --textbox "$LFILE" 0 0
  suid:
    - code: |
        LFILE=file_to_read
        ./dialog --textbox "$LFILE" 0 0
  sudo:
    - code: |
        LFILE=file_to_read
        sudo dialog --textbox "$LFILE" 0 0
---
