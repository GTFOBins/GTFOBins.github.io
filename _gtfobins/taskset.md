---
functions:
  exec-interactive:
    - code: taskset 1 /bin/sh
  sudo-enabled:
    - code: sudo taskset 1 /bin/sh
  suid-enabled:
    - code: ./taskset 1 /bin/sh -p
---