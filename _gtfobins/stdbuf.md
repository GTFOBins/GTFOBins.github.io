---
functions:
  execute-interactive:
  - code: stdbuf -i0 /bin/sh
  suid-enabled:
  - code: "./stdbuf -i0 /bin/sh -p"
  sudo-enabled:
  - code: sudo stdbuf -i0 /bin/sh
---
