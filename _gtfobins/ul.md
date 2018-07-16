---
description: The read file content is corrupted by replacing occurrences of `$'\b_'` to terminal sequences and by converting tabs to spaces.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        ul "$LFILE"
  suid-enabled:
    - code: |
        LFILE=file_to_read
        ./ul "$LFILE"
  sudo-enabled:
    - code: |
        LFILE=file_to_read
        sudo ul "$LFILE"
---
