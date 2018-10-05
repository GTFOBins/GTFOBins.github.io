---
functions:
  shell:
    - code: env /bin/sh
  suid:
    - code: ./env /bin/sh -p
  sudo:
    - code: sudo env /bin/sh
---
