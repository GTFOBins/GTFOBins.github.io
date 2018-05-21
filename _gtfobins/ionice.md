---
functions:
  exec-interactive:
    - code: ionice /bin/sh
  sudo-enabled:
    - code: sudo ionice /bin/sh
  suid-enabled:
    - code: ./ionice /bin/sh -p
---