---
functions:
  execute-interactive:
    - code: timeout 7d /bin/sh
  suid-enabled:
    - code: ./timeout 7d /bin/sh -p
  sudo-enabled:
    - code: sudo timeout --foreground 7d /bin/sh
---
