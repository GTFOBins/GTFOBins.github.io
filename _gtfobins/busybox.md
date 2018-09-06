---
description: BusyBox may contain many UNIX utilities, run `busybox --list-full` to check what GTFBins binaries are supported. Here some example.
functions:
  execute-interactive:
    - code: busybox sh
  upload:
    - description: Serve files in the local folder running an HTTP server.
      code: |
        export LPORT=12345
        busybox httpd -f -p $LPORT -h .
  file-write:
    - code: |
        LFILE=file_to_write
        busybox sh -c 'echo "DATA" > $LFILE'
  file-read:
    - code: |
        LFILE=file_to_read
        ./busybox cat "$LFILE"
  suid-enabled:
    - description: It may drop the SUID privileges depending on the compilation flags and the runtime configuration.
      code: "./busybox sh"
  sudo-enabled:
    - code: sudo busybox sh
---
