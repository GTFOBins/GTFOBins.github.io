---
functions:
  execute-interactive:
    - code: gdb -nx -ex '!sh' -ex quit
  sudo-enabled:
    - code: sudo gdb -nx -ex '!sh' -ex quit
---
