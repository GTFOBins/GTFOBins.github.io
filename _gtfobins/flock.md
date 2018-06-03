---
functions:
  execute-interactive:
    - code: flock /tmp /bin/sh
  sudo-enabled:
    - code: sudo flock /tmp /bin/sh
  suid-enabled:
    - code: ./flock /tmp /bin/sh -p
---
