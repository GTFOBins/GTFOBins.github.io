---
functions:
  exec-interactive:
    - code: strace -o /dev/null /bin/sh
  sudo-enabled:
    - code: sudo strace -o /dev/null /bin/sh
  suid-enabled:
    - code: ./strace -o /dev/null /bin/sh -p
---
