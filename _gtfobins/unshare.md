---
functions:
  shell:
    - code: unshare /bin/sh
  suid:
    - code: ./unshare -r /bin/sh
  sudo:
    - code: sudo unshare /bin/sh
---
