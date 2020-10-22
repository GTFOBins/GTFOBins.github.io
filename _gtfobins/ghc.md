---
functions:
  shell:
    - code: ghc -e 'System.Process.callCommand "/bin/bash"'
  sudo:
    - code: sudo ghc -e 'System.Process.callCommand "/bin/bash"'
---
