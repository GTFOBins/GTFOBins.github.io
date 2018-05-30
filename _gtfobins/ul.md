---
description: The read file content is corrupted by replacing the occurrences of underscores to terminal sequences.
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
