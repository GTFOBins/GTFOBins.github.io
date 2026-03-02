---
functions:
  command:
  - code: |-
      nohup /path/to/command
      cat nohup.out
    comment: |-
      The `nohup.out` file contains the standard output and error of the command.
    contexts:
      sudo:
      suid:
      unprivileged:
  shell:
  - code: |-
      nohup /bin/sh -c '/bin/sh </dev/tty >/dev/tty 2>/dev/tty'
    comment: |-
      This creates a `nohup.out` file in the current working directory.
    contexts:
      sudo:
      suid:
        code: |-
          nohup /bin/sh -p -c '/bin/sh -p </dev/tty >/dev/tty 2>/dev/tty'
        shell: false
      unprivileged:
...
