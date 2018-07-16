---
functions:
  execute-interactive:
    - code: csh
  file-write:
    - code: |
        export LFILE=file_to_write
        ash -c 'echo data > $LFILE'
  suid-enabled:
    - code: "./csh -b"
  sudo-enabled:
    - code: sudo csh
---
