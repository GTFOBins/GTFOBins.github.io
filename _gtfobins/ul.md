---
description: The read file content is corrupted by replacing occurrences of `$'\b_'` to terminal sequences and by converting tabs to spaces.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        ul "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./ul "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo ul "$LFILE"
---
