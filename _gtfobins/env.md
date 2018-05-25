---
functions:
  execute-interactive:
    - code: env /bin/sh
  sudo-enabled:
    - code: sudo env /bin/sh
  suid-enabled:
    - code: ./env /bin/sh -p
---
