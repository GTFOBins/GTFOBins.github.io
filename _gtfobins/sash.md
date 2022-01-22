---
functions:
  shell:
    - code: sash -c '/bin/sh'
  suid:
    - code: ./sash -c '/bin/sh -p'
  limited-suid:
    - code: ./sash -c '/bin/sh'
  sudo:
    - code: sudo sash -c '/bin/sh'
---
