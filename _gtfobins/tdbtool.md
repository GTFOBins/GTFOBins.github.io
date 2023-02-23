---
functions:
  shell:
    - code: |
        tdbtool
        ! /bin/sh
  sudo:
    - code: |
        sudo tdbtool
        ! /bin/sh
  limited-suid:
    - code: |
        ./tdbtool
        ! /bin/sh
---
