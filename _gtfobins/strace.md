---
functions:
  execute-interactive:
    - code: strace -o /dev/null /bin/sh
  suid-enabled:
    - code: ./strace -o /dev/null /bin/sh -p
  sudo-enabled:
    - code: sudo strace -o /dev/null /bin/sh
---
