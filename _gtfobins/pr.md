---
description: Some bytes are altered so it might not be suitable for binary files.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        pr -T $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        pr -T $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        pr -T $LFILE
---
