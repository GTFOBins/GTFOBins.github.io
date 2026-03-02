---
functions:
  file-read:
  - code: |-
      more /path/to/input-file
    comment: |-
      The file is displayed in the terminal interface.
    contexts:
      sudo:
      suid:
      unprivileged:
  shell:
  - code: |-
      more /etc/hosts
      !/bin/sh
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
...
