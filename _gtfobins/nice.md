---
functions:
  execute-interactive:
    - code: nice /bin/sh
  suid-enabled:
    - code: ./nice /bin/sh -p
  sudo-enabled:
    - code: sudo nice /bin/sh
---
