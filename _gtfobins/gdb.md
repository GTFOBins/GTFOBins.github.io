---
functions:
  execute-interactive:
    - code: gdb -nx -ex '!sh' -ex quit
  sudo-enabled:
    - code: sudo gdb -nx -ex '!sh' -ex quit
  file-write:
    - code: |
        LFILE=file_to_write
        gdb -nx -ex "dump value $LFILE \"data\"" -ex quit
---
