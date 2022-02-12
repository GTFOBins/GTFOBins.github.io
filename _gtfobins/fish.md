---
functions:
  shell:
    - code: fish -c '/bin/sh'
  suid:
    - code: ./fish -c '/bin/sh -p'
  sudo:
    - code: sudo fish -c '/bin/sh'
---
