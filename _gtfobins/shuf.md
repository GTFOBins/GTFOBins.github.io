---
description: The read file content is corrupted by adding a newline.
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_write
        sudo shuf -e data -o "$LFILE"
  suid-enabled:
    - description:
      code: |
        LFILE=file_to_write
        ./shuf -e data -o "$LFILE"
  file-write:
    - code: |
        LFILE=file_to_write
        shuf -e data -o "$LFILE"
---
