---
functions:
  exec-interactive:
    - code: |
        wish
        exec /bin/sh <@stdin >@stdout 2>@stderr
  sudo-enabled:
    - code: |
        sudo wish
        exec /bin/sh <@stdin >@stdout 2>@stderr
---