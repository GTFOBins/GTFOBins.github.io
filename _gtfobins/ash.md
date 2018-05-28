---
functions:
  execute-interactive:
    - code: ash
  sudo-enabled:
    - code: sudo ash
  suid-enabled:
    - code: ./ash
  file-write:
    - code: |
        export LFILE=file_to_write
        ash -c 'echo data > $LFILE'
---
