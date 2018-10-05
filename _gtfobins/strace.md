---
functions:
  shell:
    - code: strace -o /dev/null /bin/sh
  suid:
    - code: ./strace -o /dev/null /bin/sh -p
  sudo:
    - code: sudo strace -o /dev/null /bin/sh
---
