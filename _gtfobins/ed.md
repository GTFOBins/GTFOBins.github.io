---
functions:
  execute-interactive:
    - code: |
        ed
        !/bin/sh
  sudo-enabled:
    - code: |
        sudo ed
        !/bin/sh
  suid-limited:
    - code: |-
        ./ed
        !/bin/sh
---
