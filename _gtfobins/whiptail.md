---
description: The file is shown in an interactive TUI dialog, thus it is not suitable for binary/too big data.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        whiptail --textbox "$LFILE" 20 0
  suid:
    - code: |
        LFILE=file_to_read
        ./whiptail --textbox "$LFILE" 20 0
  sudo:
    - code: |
        LFILE=file_to_read
        sudo whiptail --textbox "$LFILE" 20 0
---
