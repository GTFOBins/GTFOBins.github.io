---
functions:
  command:
    - code: |
        COMMAND='/usr/bin/id'
        nohup "$COMMAND"
        cat nohup.out
  sudo:
    - code: |
        COMMAND='/usr/bin/id'
        sudo nohup "$COMMAND"
        sudo cat nohup.out
---
