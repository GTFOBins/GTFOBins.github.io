---
functions:
  sudo:
    - description: A temporary directory is created to not mess around with the current installation. The certbot server has to be reachable. The command output is visible in the certbot output.
      code: |
        COMMAND='id'
        TF=$(mktemp -d)
        sudo certbot certonly --standalone -n --dry-run -d example.net --work-dir $TF --config-dir $TF --agree-tos --register-unsafely-without-email --pre-hook "$COMMAND"
---
