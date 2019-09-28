---
description: This requires `iftop` 1.17 and the privilege to capture on some device (specify with `-i` if needed) .
functions:
  shell:
    - code: |
        iftop
        !/bin/sh
  limited-suid:
    - code: |
        ./iftop
        !/bin/sh
  sudo:
    - code: |
        sudo iftop
        !/bin/sh
---
