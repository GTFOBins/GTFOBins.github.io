---
description: |
  Each line is corrupted by a prefix string and wrapped inside quotes, so this may not be suitable for binary files.

  If a line in the target file begins with a `#`, it will not be printed as these lines are parsed as comments.

  It can also be provided with a directory and will read each file in the directory.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        file -m $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./file -m $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo file -m $LFILE
---
