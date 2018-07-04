---
functions:
  execute-interactive:
  - code: flock -u / /bin/sh
  suid-enabled:
  - code: "./flock -u / /bin/sh -p"
  sudo-enabled:
  - code: sudo flock -u / /bin/sh
---
