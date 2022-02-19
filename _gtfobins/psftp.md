---
functions:
  shell:
    - code: |
        psftp
        !/bin/sh
  limited-suid:
    - code: |
        sudo psftp
        !/bin/sh
  sudo:
    - code: |
        sudo psftp
        !/bin/sh
---
