---
functions:
  shell:
    - code: multitime /bin/sh
  suid:
    - code: ./multitime /bin/sh -p
  sudo:
    - code: sudo multitime /bin/sh
---
