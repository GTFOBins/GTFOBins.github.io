---
description: This can be used to read or write files outside a restricted file systems or with elevated privileges.
functions:
  file-write:
    - code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        mv $TF $LFILE
  file-read:
    - code: |
        LFILE=file_to_read
        TF=$(mktemp)
        mv $LFILE $TF
        cat $TF
  suid-enabled:
    - code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        ./mv $TF $LFILE
  sudo-enabled:
    - code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        sudo mv $TF $LFILE
---
