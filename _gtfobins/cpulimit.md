---
functions:
  execute-interactive:
    - code: cpulimit -l 100 -f /bin/sh
  execute-non-interactive:
    - description: By default, commands are executed in the background
      code: cpulimit -l 100 whoami
  sudo-enabled:
    - code: sudo cpulimit -l 100 -f /bin/sh
---
