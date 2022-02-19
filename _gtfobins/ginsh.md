---
functions:
  shell:
    - code: |
        ginsh
        !/bin/sh
  limited-suid:
    - code: |
        ./ginsh
        !/bin/sh
  sudo:
    - code: |
        sudo ginsh
        !/bin/sh
---
