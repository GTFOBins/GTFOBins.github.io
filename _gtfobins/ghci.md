---
functions:
  shell:
    - code: |
       ghci
       System.Process.callCommand "/bin/sh"
  sudo:
    - code: |
       sudo ghci
       System.Process.callCommand "/bin/sh"
---
