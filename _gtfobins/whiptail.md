---
description: The file is shown in an interactive TUI dialog made for displaying text, arrows can be used to scroll long content.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        whiptail --textbox --scrolltext "$LFILE" 0 0
  suid:
    - code: |
        LFILE=file_to_read
        ./whiptail --textbox --scrolltext "$LFILE" 0 0
  sudo:
    - code: |
        LFILE=file_to_read
        sudo whiptail --textbox --scrolltext "$LFILE" 0 0
---
