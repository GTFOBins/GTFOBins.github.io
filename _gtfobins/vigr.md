---
description: This command allows to edit some designated files (`/etc/passwd`, `/etc/group`, `/etc/shadow` and `/etc/gshadow`) safely by spawning the default editor (falling back to [`vim`](/gtfobins/vim/), other functions may apply). Despite requiring superuser privileges to run, the editor is executed as the unprivileged user when run as SUID or with `sudo`.
functions:
  suid:
    - code: ./vigr
  sudo:
    - code: sudo vigr
---
