---
description: The file is shown in an interactive TUI dialog, thus it is not suitable for binary/too big data.
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
