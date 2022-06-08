---
description: The interaction happens in a GUI window, while the shell is dropped in the terminal.
functions:
  shell:
    - code: |
        zathura
        :! /bin/sh -c 'exec /bin/sh 0<&1'
  sudo:
    - code: |
        sudo zathura
        :! /bin/sh -c 'exec /bin/sh 0<&1'
---
