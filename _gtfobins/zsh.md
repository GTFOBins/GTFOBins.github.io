---
functions:
  file-read:
    - code: |
        export LFILE=file_to_read
        zsh -c 'echo "$(<$LFILE)"'
  file-write:
    - code: |
        export LFILE=file_to_write
        zsh -c 'echo DATA >$LFILE'
  shell:
    - code: zsh
  suid:
    - code: ./zsh
  sudo:
    - code: sudo zsh
---
