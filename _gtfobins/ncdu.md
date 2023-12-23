---
functions:
  shell:
    - code: |
        ncdu
        b
  sudo:
    - code: |
        sudo ncdu
        b
  limited-suid:
    - code: |
        ./ncdu
        b
---
