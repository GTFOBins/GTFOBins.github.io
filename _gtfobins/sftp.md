---
functions:
  exec-interactive:
    - code: |
        HOST=user@10.0.0.1
        sftp $HOST
        !/bin/sh
  sudo-enabled:
    - code: |
        HOST=user@10.0.0.1
        sudo sftp $HOST
        !/bin/sh
  upload:
    - description: Send local file to a SSH server.
      code: |
        RHOST=user@10.0.0.1
        sftp $RHOST
        put file_to_send where_to_save
  download:
    - description: Fetch a remote file from a SSH server.
      code: |
        RHOST=user@10.0.0.1
        sftp $RHOST
        get file_to_get where_to_save
---
