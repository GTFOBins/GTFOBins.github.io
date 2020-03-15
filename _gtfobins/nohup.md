---
functions:
  command:
    - code: |
        export COMMAND='/usr/bin/id'
        nohup "$COMMAND"
        cat nohup.out
  sudo:
    - code: |
        export COMMAND='/usr/bin/id'
        sudo nohup "$COMMAND"
        sudo cat nohup.out
---
