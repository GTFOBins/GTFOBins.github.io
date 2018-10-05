---
functions:
  shell:
    - code: cpulimit -l 100 -f /bin/sh
  sudo:
    - code: sudo cpulimit -l 100 -f /bin/sh
---
