---
functions:
  file-read:
  - code: |-
      xxd /path/to/input-file | xxd -r
    contexts:
      sudo:
      suid:
      unprivileged:
  file-write:
  - code: |-
      echo DATA | xxd | xxd -r - /path/to/output-file
    contexts:
      sudo:
      suid:
      unprivileged:
...
