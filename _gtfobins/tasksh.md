---
functions:
  shell:
    - code: |
        tasksh
        !/bin/sh
  limited-suid:
    - code: |
        ./tasksh
        !/bin/sh
  sudo:
    - code: |
        sudo tasksh
        !/bin/sh
---
