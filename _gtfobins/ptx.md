---
description: While the program is capable of reading the file, it outputs a "permuted index" of its content, thus altering it. Adjusting the options could yield more readable outputs.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        ptx -w 5000 "$LFILE"
  suid:
    - code: |
        LFILE=file_to_read
        ./ptx -w 5000 "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo ptx -w 5000 "$LFILE"
---
