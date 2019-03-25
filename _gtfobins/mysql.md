---
description: A valid MySQL server must be available.
functions:
  shell:
    - code: mysql -e '\! /bin/sh'
  sudo:
    - code: sudo mysql -e '\! /bin/sh'
  limited-suid:
    - code: ./mysql -e '\! /bin/sh'
  library-load:
    - description: |
        A MySQL server must accept connections in order for this to work.

        The following loads the `/path/to/lib.so` shared object.
      code: mysql --default-auth ../../../../../path/to/lib
---
