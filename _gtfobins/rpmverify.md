---
functions:
  shell:
    - code: rpmverify --eval '%(bash 1>&2)'
  limited-suid:
    - code: ./rpmverify --eval '%(bash 1>&2)'
  sudo:
    - code: sudo rpmverify --eval '%(bash 1>&2)'
---
