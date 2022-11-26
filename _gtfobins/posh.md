---
functions:
  shell:
    - code: posh -c /bin/sh
  limited-suid:
    - code: ./posh -c '/bin/sh -p'
  sudo:
    - code: sudo posh -c /bin/sh
---
