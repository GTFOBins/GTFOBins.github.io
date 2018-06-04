---
description: |
  Note that the shell might have its own builtin time implementation, which may
  behave differently than /usr/bin/time.
functions:
  execute-interactive:
    - code: /usr/bin/time /bin/sh
  sudo-enabled:
    - code: sudo /usr/bin/time /bin/sh
  suid-enabled:
    - code: ./time /bin/sh -p
---
