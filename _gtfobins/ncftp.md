---
functions:
  shell:
    - code: |
        ncftp
        !/bin/sh
  limited-suid:
    - code: |
        sudo ncftp
        !/bin/sh -p
  sudo:
    - code: |
        sudo ncftp
        !/bin/sh
---
