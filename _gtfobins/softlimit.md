---
functions:
  shell:
    - code: softlimit /bin/sh
  suid:
    - code: ./softlimit /bin/sh -p
  sudo:
    - code: sudo softlimit /bin/sh
---
