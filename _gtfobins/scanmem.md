---
functions:
  shell:
    - code: |
        scanmem
        shell /bin/sh
  suid:
    - code: |
        ./scanmem
        shell /bin/sh
  sudo:
    - code: |
        sudo scanmem
        shell /bin/sh
---
