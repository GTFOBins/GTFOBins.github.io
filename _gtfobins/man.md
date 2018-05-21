---
functions:
  exec-interactive:
    - code: |
        man man
        !/bin/sh
  sudo-enabled:
    - code: |
        sudo man man
        !/bin/sh
  suid-limited:
    - code: |-
        ./man man
        !/bin/sh -p
---