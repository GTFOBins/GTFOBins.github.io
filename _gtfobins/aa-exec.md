---
functions:
  shell:
    - code: aa-exec /bin/sh
  suid:
    - code: ./aa-exec /bin/sh -p
  sudo:
    - code: sudo aa-exec /bin/sh
---
