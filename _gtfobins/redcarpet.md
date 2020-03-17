---
description: The file is actually parsed as a Markdown file.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        redcarpet "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo redcarpet "$LFILE"
---
