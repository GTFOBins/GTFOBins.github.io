---
functions:
  execute-interactive:
  - code: unshare /bin/sh
  suid-enabled:
  - code: "./unshare -r /bin/sh"
  sudo-enabled:
  - code: sudo unshare /bin/sh
---
