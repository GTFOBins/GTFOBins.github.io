---
functions:
  execute-interactive:
    - code: emacs -Q -nw --eval '(term "/bin/sh")'
  sudo-enabled:
    - code: sudo emacs -Q -nw --eval '(term "/bin/sh")'
  suid-enabled:
    - code: ./emacs -Q -nw --eval '(term "/bin/sh -p")'
  file-read: 
    - code: |
        emacs file_to_read
  file-write: 
    - code: |
        emacs file_to_write
        C-x C-s
---
