---
functions:
  execute-interactive:
    - code: dash
  sudo-enabled:
    - code: sudo dash
  suid-enabled:
    - code: ./dash -p
  file-write:
    - code: |
        export LFILE=file_to_write
        ash -c 'echo data > $LFILE'
---
