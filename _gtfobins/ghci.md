---
functions:
  shell:
    - code: |
       ghci
       Prelude> System.Process.callCommand "/bin/bash"
  sudo:
    - code: |
       sudo ghci
       Prelude> System.Process.callCommand "/bin/bash"
---
