---
description: |
 The file is typeset but text is still readable in the output, alternatively the output can be read with `man -l`.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        troff $LFILE
  suid:
    - code: |
        LFILE=file_to_read
        ./troff $LFILE
  sudo:
    - code: |
        LFILE=file_to_read
        sudo troff $LFILE
---
