---
description: This includes the file in the actual configuration file, the first line is leaked as an error message.
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        apache2ctl -c "Include $LFILE" -k stop
  sudo:
    - code: |
        LFILE=file_to_read
        sudo apache2ctl -c "Include $LFILE" -k stop
---
