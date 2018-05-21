---
functions:
  exec-interactive:
    - code: |
        tclsh
        exec /bin/sh <@stdin >@stdout 2>@stderr
  sudo-enabled:
    - code: |
        sudo tclsh
        exec /bin/sh <@stdin >@stdout 2>@stderr
  suid-enabled:
    - code: |
        ./tclsh
        exec /bin/sh -p <@stdin >@stdout 2>@stderr
---