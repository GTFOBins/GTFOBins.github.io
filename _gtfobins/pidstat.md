---
functions:
  command:
    - code: |
        COMMAND=id
        pidstat -e $COMMAND
  sudo:
    - code: |
        COMMAND=id
        sudo pidstat -e $COMMAND
  suid:
    - code: |
        COMMAND=id
        ./pidstat -e $COMMAND
---
