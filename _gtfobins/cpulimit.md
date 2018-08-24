---
functions:
  execute-interactive:
    - code: cpulimit -l 100 -f /bin/sh
  sudo-enabled:
    - code: sudo cpulimit -l 100 -f /bin/sh
---
