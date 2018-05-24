---
functions:
  exec-interactive:
    - code: expect -c 'spawn /bin/sh;interact'
  sudo-enabled:
    - code: sudo expect -c 'spawn /bin/sh;interact'
  suid-enabled:
    - code: ./expect -c 'spawn /bin/sh -p;interact'
---
