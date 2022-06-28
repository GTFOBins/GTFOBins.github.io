---
functions:
  shell:
    - code: rpmverify --eval '%(/bin/sh 1>&2)'
  limited-suid:
    - code: ./rpmverify --eval '%(/bin/sh 1>&2)'
  sudo:
    - code: sudo rpmverify --eval '%(/bin/sh 1>&2)'
---
