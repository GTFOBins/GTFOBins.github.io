---
description: change group ownership.
functions:
  suid:
    - code: |
        LFILE=file_to_change
        ./chgrp $(id -gn) $LFILE
  sudo:
    - code: |
        LFILE=file_to_change
        sudo chgrp $(id -gn) $LFILE
---
