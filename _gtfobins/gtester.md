---
functions:
  command:
    - code: |
        TF=$(mktemp)
        echo '#!/bin/sh' > $TF
        echo '/usr/bin/id' >> $TF
        chmod +x $TF
        gtester -q $TF
  sudo:
    - code: |
        TF=$(mktemp)
        echo '#!/bin/sh' > $TF
        echo '/usr/bin/id' >> $TF
        chmod +x $TF
        sudo gtester -q $TF
---
