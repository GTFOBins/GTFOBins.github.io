---
functions:
  shell:
    - code: capsh --
  suid:
    - code: ./capsh --gid=0 --uid=0 --
  sudo:
    - code: sudo capsh --
---
