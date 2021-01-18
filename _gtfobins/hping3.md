---
functions:
  shell:
    - code: |
        hping3
        /bin/sh
  suid:
    - code: |
        ./hping3
        /bin/sh -p
  sudo:
    - code: |
        sudo hping3
        /bin/sh
---
