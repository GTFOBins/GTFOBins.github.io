---
functions:
  execute-interactive:
  - code: env /bin/sh
  suid-enabled:
  - code: "./env /bin/sh -p"
  sudo-enabled:
  - code: sudo env /bin/sh
---
