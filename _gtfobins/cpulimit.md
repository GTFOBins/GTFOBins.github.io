---
functions:
  execute-interactive:
    - description: With -f, the commands are executed in the terminal you start them. -l 100 specified that the command is to use a single CPU core
    - code: cpulimit -l 100 -f /bin/sh
  execute-non-interactive:
    - description: With -b, which is the default, commands are executed in the background
      code: cpulimit -l 100 whoami
---
