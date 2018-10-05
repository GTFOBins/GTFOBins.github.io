---
functions:
  shell:
    - code: timeout 7d /bin/sh
  suid:
    - code: ./timeout 7d /bin/sh -p
  sudo:
    - code: sudo timeout --foreground 7d /bin/sh
---
