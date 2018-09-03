---
description: This can be used to read or write files outside a restricted file systems or with elevated privileges.
functions:
  file-write:
    - code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        cp $TF $LFILE
  file-read:
    - code: |
        LFILE=file_to_read
        TF=$(mktemp)
        cp $LFILE $TF
        cat $TF
  suid-enabled:
    - code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        ./cp $TF $LFILE
  sudo-enabled:
    - code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        sudo cp $TF $LFILE
---
