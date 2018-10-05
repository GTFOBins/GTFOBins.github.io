---
functions:
  shell:
    - code: ltrace -b -L /bin/sh
  sudo:
    - code: sudo ltrace -b -L /bin/sh
---
