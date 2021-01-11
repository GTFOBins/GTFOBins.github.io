---
functions:
  shell:
    - code: |
        hping3
        /bin/sh
  sudo:
    - code: |
        sudo hping3
        /bin/sh
  limited-suid:
    - code: |
        ./hping3
        /bin/sh
---
