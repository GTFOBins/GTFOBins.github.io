---
functions:
  execute-interactive:
    - code: ash
  file-write:
    - code: |
        export LFILE=file_to_write
        ash -c 'echo DATA > $LFILE'
  suid-enabled:
    - code: "./ash"
  sudo-enabled:
    - code: sudo ash
---
