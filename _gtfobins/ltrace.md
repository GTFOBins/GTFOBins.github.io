---
functions:
  execute-interactive:
  - code: ltrace -b -L /bin/sh
  sudo-enabled:
  - code: sudo ltrace -b -L /bin/sh
---
