---
functions:
  execute-interactive:
    - code: csh
  sudo-enabled:
    - code: sudo csh
  suid-enabled:
    - code: ./csh -b
  file-write:
    - code: |
        export LFILE=file_to_write
        ash -c 'echo data > $LFILE'
---
