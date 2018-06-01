---
description: |
  The read file content is corrupted by replacing occurrences of `$'\b_'` to
  terminal sequences and by converting tabs to spaces.
functions:
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo ul "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./ul "$LFILE"
  file-read:
    - code: |
        LFILE=file_to_read
        ul "$LFILE"
---
