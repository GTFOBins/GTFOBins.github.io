---
functions:
  suid:
    - code: |
        sudo install acr $(which acr) .
        touch Makefile && chmod + Makefile
        echo DATA > Makefile
        ./acr -r Makefile
  sudo:
    - code: |
        sudo install acr $(which acr) .
        touch Makefile && chmod + Makefile
        echo DATA > Makefile
        sudo acr -r Makefile
---
