---
functions:
  file-read:
  - binary: false
    code: |-
      ed /path/to/input-file
      ,p
      q
    contexts:
      sudo:
      suid:
      unprivileged:
  file-write:
  - binary: false
    code: |-
      ed /path/to/output-file
      a
      DATA
      .
      w
      q
    contexts:
      sudo:
      suid:
      unprivileged:
  shell:
  - code: |-
      ed
      !/bin/sh
      q
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
...
