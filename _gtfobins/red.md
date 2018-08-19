---
description: Short for "restricted ed".
functions:
  execute-interactive:
    - code: |
        red
        !/bin/sh
  file-write:
    - code: |
        red file_to_write
        w
  sudo-enabled:
    - code: |
        sudo red
        !/bin/sh
  suid-limited:
    - code: |
        ./red
        !/bin/sh
---
