---
functions:
  file-read:
  - code: |-
      man /path/to/input-file
    comment: |-
      The file is shown somehow formatted and displayed in the default pager.
    contexts:
      sudo:
      suid:
      unprivileged:
  inherit:
  - code: |-
      man man
    contexts:
      sudo:
      suid:
      unprivileged:
    from: less
  shell:
  - code: |-
      man '-H/bin/sh #' man
    comment: |-
      This requires GNU `troff` (`groff`) to be installed.
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
    version: |-
      GNU
...
