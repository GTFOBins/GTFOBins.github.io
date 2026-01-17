---
functions:
  file-write:
  - binary: false
    code: |-
      rlwrap -l /path/to/output-file echo DATA
    comment: |-
      This adds timestamps to the output file. This relies on the external `echo` command.
    contexts:
      sudo:
      suid:
      unprivileged:
  shell:
  - code: |-
      rlwrap /bin/sh
    contexts:
      sudo:
      suid:
        code: |-
          rlwrap /bin/sh -p
        shell: false
      unprivileged:
...
