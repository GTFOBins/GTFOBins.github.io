---
functions:
  execute-interactive:
    - code: dash
  file-write:
    - code: |
        export LFILE=file_to_write
        ash -c 'echo data > $LFILE'
  suid-enabled:
    - code: ./dash -p
  sudo-enabled:
    - code: sudo dash
---
