---
description: This includes the file in the actual configuration file, the first line is leaked as an error message.
functions:
  sudo:
    - code: |
        LFILE=file_to_read
        sudo apache2 -f $LFILE
---
