---
description: The content is actually parsed and corrupted by the command, thus it may not be suitable for arbitrary files.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        eqn "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./eqn "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo eqn "$LFILE"
---
