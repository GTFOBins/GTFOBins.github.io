---
functions:
  shell:
    - code: ssh-agent /bin/sh
  suid:
    - code: ./ssh-agent /bin/ -p
  sudo:
    - code: sudo ssh-agent /bin/
---
