---
description: The file content appears in the middle of other textual information, thus it might not be suitable to read arbitray binary files.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        espeak -qXf "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./espeak -qXf "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo espeak -qXf "$LFILE"
---
