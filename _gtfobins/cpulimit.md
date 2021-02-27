---
functions:
  shell:
    - code: cpulimit -l 100 -f /bin/sh
  suid:
    - code: ./cpulimit -l 100 -f -- /bin/sh -p
  sudo:
    - code: sudo cpulimit -l 100 -f /bin/sh
---
