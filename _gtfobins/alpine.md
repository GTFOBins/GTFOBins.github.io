---
description: The file is displayed in the `alpine` curses terminal interface. Other options might be available, for example by pressing `S` is possible to save the file content elsewhere.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        alpine -F "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./alpine -F "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo alpine -F "$LFILE"
---
