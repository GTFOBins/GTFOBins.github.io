---
functions:
  exec-interactive:
    - code: |
        less /etc/profile
        !/bin/sh
    - code: |
        VISUAL="/bin/sh -c '/bin/sh'" less /etc/profile
        v
  sudo-enabled:
    - code: |
        sudo less /etc/profile
        !/bin/sh
  suid-limited:
    - code: |-
        ./less /etc/profile
        !/bin/sh
---
