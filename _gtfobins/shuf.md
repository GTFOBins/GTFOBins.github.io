---
description: The read file content is corrupted by adding a newline.
functions:
  file-write:
    - code: |
        LFILE=file_to_write
        shuf -e DATA -o "$LFILE"
  suid:
    - code: |
        LFILE=file_to_write
        ./shuf -e DATA -o "$LFILE"
        sudo:
    - code: |
        LFILE=file_to_write
        sudo shuf -e DATA -o "$LFILE"
---
