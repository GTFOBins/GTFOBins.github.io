---
functions:
  command:
    - code: |
        COMMAND=id
        nvim -c ':!'$COMMAND
  sudo:
    - code: |
        sudo nvim -c ':terminal'
---
