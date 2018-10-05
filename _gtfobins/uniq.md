---
description: The read file content is corrupted by squashing multiple adjacent lines.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        uniq "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./uniq "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo uniq "$LFILE"
---
