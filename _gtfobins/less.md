---
functions:
  execute-interactive:
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
  file-read: 
    - code: |
        less file_to_read
---
