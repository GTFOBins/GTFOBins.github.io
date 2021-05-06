---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        gcc -x c -E "$LFILE"
  file-write:  # XXX this should be file-delete
    - code: |
        LFILE=file_to_delete
        gcc -xc /dev/null -o $LFILE
  shell:
    - code: gcc -wrapper /bin/sh,-s .
  sudo:
    - code: sudo gcc -wrapper /bin/sh,-s .
---
