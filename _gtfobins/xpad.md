---
description: This is a GUI application. The file content is displayed in a sticky note.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        xpad -f "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo xpad -f "$LFILE"
---
