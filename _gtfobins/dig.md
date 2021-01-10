---
description: Each input line is treated as a lookup query for the `dig` command and the output is corrupted with the result or errors of the operation, so this may not be suitable for binary files. Grepping for `DiG` might help to filter out unwanted content.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        dig -f $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo dig -f $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./dig -f $LFILE
---
