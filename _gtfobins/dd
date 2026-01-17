---
functions:
  file-read:
  - code: |-
      dd if=/path/to/input-file
    contexts:
      sudo:
      suid:
      unprivileged:
  file-write:
  - code: |-
      echo DATA | dd of=/path/to/output-file
    contexts:
      sudo:
      suid:
      unprivileged:
...
