---
description: Note that the shell might have its own builtin time implementation, which may behave differently than` /usr/bin/time`, hence the absolute path.
functions:
  shell:
    - code: /usr/bin/time /bin/sh
  suid:
    - code: ./time /bin/sh -p
  sudo:
    - code: sudo /usr/bin/time /bin/sh
---
